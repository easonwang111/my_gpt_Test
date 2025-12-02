"""Textual HUD renderer.

In a GUI environment this would draw to the screen; for the purpose of this
prototype it emits formatted strings that can be printed or logged.  The
`render_snapshot` method is intentionally simple so it can run in text-only
contexts.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from .entities import Character, Weapon


@dataclass
class HudLine:
    text: str


@dataclass
class HudState:
    lines: List[HudLine]

    def as_text(self) -> str:
        return "\n".join(line.text for line in self.lines)


def summarize_weapon(weapon: Weapon) -> str:
    return (
        f"{weapon.name} | DMG {weapon.damage} | PEN {weapon.penetration:.2f} |"
        f" MAG {weapon.state.bullets_left}/{weapon.magazine_size}"
    )


def render_snapshot(actors: Iterable[Character]) -> HudState:
    lines: List[HudLine] = []
    for actor in actors:
        weapon = actor.current_weapon()
        lines.append(
            HudLine(
                text=(
                    f"{actor.name}: HP {actor.health} | ARM {actor.armor} | MONEY "
                    f"{actor.money} | {summarize_weapon(weapon)}"
                )
            )
        )
    return HudState(lines)
