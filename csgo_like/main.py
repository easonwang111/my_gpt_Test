"""Entry point for the prototype.

This module wires together the engine loop, a couple of characters, and the HUD
renderer.  Running it will execute a brief simulation showcasing movement and
firing logic in text form.
"""
from __future__ import annotations

import time
from itertools import cycle

from .config import ROUND_TIME_SECONDS
from .engine import GameLoop
from .entities import Bot, Character, Vector2
from .hud import render_snapshot
from .weapons import CATALOGUE


class CombatSimulation:
    """A small subsystem that advances character state."""

    def __init__(self, actors: list[Character]):
        self.actors = actors
        self._directions = cycle([
            Vector2(1, 0),
            Vector2(-1, 0),
            Vector2(0, 1),
            Vector2(0, -1),
        ])

    def update(self, dt: float) -> None:
        for actor in self.actors:
            direction = next(self._directions)
            actor.move(direction, dt, running=True)
            actor.tick(dt)


class HudSubsystem:
    """Renders HUD snapshots on an interval."""

    def __init__(self, actors: list[Character], interval: float = 1.0):
        self.actors = actors
        self.interval = interval
        self.time = 0.0

    def update(self, dt: float) -> None:
        self.time += dt
        if self.time >= self.interval:
            self.time = 0.0
            hud = render_snapshot(self.actors)
            print("\n" + hud.as_text())


def create_characters() -> list[Character]:
    hero = Character(name="Player", position=Vector2(0, 0), money=5000)
    rival = Bot(name="Bot", position=Vector2(15, 5))
    for weapon_name in list(CATALOGUE.keys())[:2]:
        weapon_data = CATALOGUE[weapon_name]
        hero.buy_weapon(hero.current_weapon().__class__(
            name=weapon_data.name,
            damage=weapon_data.damage,
            penetration=weapon_data.penetration,
            recoil=weapon_data.recoil,
            fire_rate=weapon_data.fire_rate,
            magazine_size=weapon_data.magazine_size,
            reload_time=weapon_data.reload_time,
            price=weapon_data.price,
        ))
    rival.target = hero
    return [hero, rival]


def run_game(round_time: float = ROUND_TIME_SECONDS) -> None:  # pragma: no cover
    actors = create_characters()
    loop = GameLoop()
    loop.add_subsystem(CombatSimulation(actors))
    loop.add_subsystem(HudSubsystem(actors, interval=2.0))
    loop.add_event(round_time, loop.stop)
    print("Starting round...\n")
    start = time.perf_counter()
    loop.run()
    print(f"Round complete in {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":  # pragma: no cover
    run_game(5.0)
