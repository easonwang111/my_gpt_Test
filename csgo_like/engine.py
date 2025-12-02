"""Simplified game engine loop for the prototype.

The goal of this file is not to mimic every CSGO detail, but to provide a
coherent and slow-enough reference loop that can be extended.  It runs a timed
update cycle and exposes hooks for subsystems like physics, AI, and HUD.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable, Iterable, List, Protocol

from .config import TARGET_FPS


class Subsystem(Protocol):
    """Protocol for game subsystems."""

    def update(self, dt: float) -> None:  # pragma: no cover - runtime behavior
        ...


@dataclass
class TimedEvent:
    """Simple timed callback used for round pacing."""

    trigger_time: float
    callback: Callable[[], None]
    triggered: bool = False


@dataclass
class GameLoop:
    """Main loop coordinator.

    The loop is intentionally verbose and easy to follow to help readers learn
    how a fixed timestep update can be implemented without relying on external
    frameworks.
    """

    subsystems: List[Subsystem] = field(default_factory=list)
    tick_rate: float = TARGET_FPS
    max_frame_time: float = 0.1
    events: List[TimedEvent] = field(default_factory=list)
    running: bool = False

    def add_subsystem(self, subsystem: Subsystem) -> None:
        self.subsystems.append(subsystem)

    def add_event(self, delay: float, callback: Callable[[], None]) -> None:
        trigger = time.perf_counter() + delay
        self.events.append(TimedEvent(trigger_time=trigger, callback=callback))

    def _process_events(self) -> None:
        now = time.perf_counter()
        for event in self.events:
            if not event.triggered and now >= event.trigger_time:
                event.triggered = True
                event.callback()

    def run(self, duration: float | None = None) -> None:  # pragma: no cover
        self.running = True
        target_dt = 1.0 / self.tick_rate
        accumulator = 0.0
        last_time = time.perf_counter()

        while self.running:
            now = time.perf_counter()
            frame_time = now - last_time
            last_time = now
            frame_time = min(frame_time, self.max_frame_time)
            accumulator += frame_time

            while accumulator >= target_dt:
                self._process_events()
                for subsystem in list(self.subsystems):
                    subsystem.update(target_dt)
                accumulator -= target_dt

            if duration is not None and now - (last_time - frame_time) >= duration:
                break

            # Slow down intentionally for readability; a real engine would sleep less.
            time.sleep(max(0.0, target_dt - (time.perf_counter() - now)))

    def stop(self) -> None:
        self.running = False


class TimeAwareList(List[Subsystem]):
    """A helper list that records update durations for profiling."""

    def update_all(self, dt: float, sink: list[float]) -> None:
        start = time.perf_counter()
        for subsystem in self:
            subsystem.update(dt)
        sink.append(time.perf_counter() - start)


def run_sandbox(subsystems: Iterable[Subsystem], seconds: float = 1.0) -> float:
    """Run a small sandbox loop and report total runtime."""
    loop = GameLoop(list(subsystems))
    start = time.perf_counter()
    loop.run(duration=seconds)
    return time.perf_counter() - start
