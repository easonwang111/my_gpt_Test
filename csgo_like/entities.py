"""Entity definitions for the prototype."""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Tuple

from .config import MovementConfig, compute_air_drag, default_weapon_config


@dataclass
class Vector2:
    x: float
    y: float

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalized(self) -> "Vector2":
        mag = self.length()
        return Vector2(self.x / mag, self.y / mag) if mag else Vector2(0, 0)


@dataclass
class WeaponState:
    bullets_left: int
    time_since_last_shot: float = 0.0


@dataclass
class Weapon:
    name: str = field(default_factory=lambda: default_weapon_config().name)
    damage: int = field(default_factory=lambda: default_weapon_config().damage)
    penetration: float = field(default_factory=lambda: default_weapon_config().penetration)
    recoil: float = field(default_factory=lambda: default_weapon_config().recoil)
    fire_rate: float = field(default_factory=lambda: default_weapon_config().fire_rate)
    magazine_size: int = field(default_factory=lambda: default_weapon_config().magazine_size)
    reload_time: float = field(default_factory=lambda: default_weapon_config().reload_time)
    price: int = field(default_factory=lambda: default_weapon_config().price)
    state: WeaponState = field(default_factory=lambda: WeaponState(default_weapon_config().magazine_size))

    def can_fire(self) -> bool:
        return self.state.bullets_left > 0 and self.state.time_since_last_shot >= 1 / self.fire_rate

    def update(self, dt: float) -> None:
        self.state.time_since_last_shot += dt

    def fire(self) -> int:
        if not self.can_fire():
            return 0
        self.state.time_since_last_shot = 0.0
        self.state.bullets_left -= 1
        spread = random.uniform(-self.recoil, self.recoil)
        return max(1, int(self.damage * (1 - abs(spread))))

    def reload(self) -> None:
        self.state.bullets_left = self.magazine_size


@dataclass
class Character:
    name: str
    position: Vector2
    velocity: Vector2 = field(default_factory=lambda: Vector2(0, 0))
    health: int = 100
    armor: int = 0
    money: int = 0
    movement: MovementConfig = field(default_factory=MovementConfig)
    inventory: List[Weapon] = field(default_factory=list)
    active_slot: int = 0

    def current_weapon(self) -> Weapon:
        if not self.inventory:
            self.inventory.append(Weapon())
        return self.inventory[self.active_slot]

    def move(self, direction: Vector2, dt: float, running: bool = False) -> None:
        speed = self.movement.run_speed if running else self.movement.walk_speed
        desired = direction.normalized() * speed
        drag = compute_air_drag(self.velocity.length())
        self.velocity = self.velocity + (desired - self.velocity) * (1 - drag)
        self.position = self.position + self.velocity * dt

    def jump(self) -> None:
        self.velocity = Vector2(self.velocity.x, self.velocity.y + self.movement.jump_force)

    def take_damage(self, amount: int) -> int:
        mitigated = max(0, amount - self.armor)
        self.health = max(0, self.health - mitigated)
        return mitigated

    def buy_weapon(self, weapon: Weapon) -> bool:
        if self.money < weapon.price:
            return False
        self.money -= weapon.price
        self.inventory.append(weapon)
        self.active_slot = len(self.inventory) - 1
        return True

    def tick(self, dt: float) -> None:
        for weapon in self.inventory:
            weapon.update(dt)


@dataclass
class Bot(Character):
    """A naive bot that randomly walks and shoots."""

    target: Character | None = None

    def update_ai(self, dt: float) -> None:
        direction = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.move(direction, dt, running=True)
        self.tick(dt)
        if self.target:
            self.shoot_at_target()

    def shoot_at_target(self) -> None:
        weapon = self.current_weapon()
        if weapon.can_fire():
            weapon.fire()


@dataclass
class Projectile:
    origin: Vector2
    direction: Vector2
    speed: float
    damage: int
    distance_traveled: float = 0.0

    def step(self, dt: float) -> None:
        self.distance_traveled += self.speed * dt


@dataclass
class Explosion:
    center: Vector2
    radius: float
    base_damage: int

    def affect(self, actors: List[Character]) -> List[Tuple[str, int]]:
        results: List[Tuple[str, int]] = []
        for actor in actors:
            delta = actor.position - self.center
            distance = delta.length()
            if distance <= self.radius:
                damage = int(self.base_damage * (1 - distance / self.radius))
                dealt = actor.take_damage(damage)
                results.append((actor.name, dealt))
        return results
