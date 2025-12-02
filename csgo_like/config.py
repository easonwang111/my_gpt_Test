"""Configuration values for the CSGO-like prototype."""
from __future__ import annotations

import math
from dataclasses import dataclass

# Basic display settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_FPS = 60

# Gameplay tuning
MAX_PLAYERS = 8
ROUND_TIME_SECONDS = 120
STARTING_MONEY = 800
GRAVITY = 9.8

@dataclass
class WeaponConfig:
    name: str
    damage: int
    penetration: float
    recoil: float
    fire_rate: float
    magazine_size: int
    reload_time: float
    price: int


def default_weapon_config() -> WeaponConfig:
    """Return a baseline weapon configuration.

    The values are intentionally generous to make the prototype easier to play.
    """
    return WeaponConfig(
        name="prototype_rifle",
        damage=35,
        penetration=0.7,
        recoil=0.1,
        fire_rate=8.0,
        magazine_size=30,
        reload_time=2.4,
        price=0,
    )


@dataclass
class MovementConfig:
    walk_speed: float = 200.0
    run_speed: float = 320.0
    crouch_speed: float = 120.0
    jump_force: float = 480.0


def compute_air_drag(speed: float) -> float:
    """Compute a tiny drag value so movement smooths out."""
    return 0.02 * speed


@dataclass
class HudColors:
    health: tuple[int, int, int] = (200, 20, 20)
    armor: tuple[int, int, int] = (30, 120, 220)
    ammo: tuple[int, int, int] = (250, 250, 250)
    crosshair: tuple[int, int, int] = (240, 240, 240)


def difficulty_curve(round_number: int) -> float:
    """Simple curve for bot difficulty scaling."""
    return 0.25 + math.log2(max(1, round_number + 1)) * 0.1
