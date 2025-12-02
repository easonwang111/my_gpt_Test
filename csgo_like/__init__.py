"""A lightweight CSGO-like prototype for educational purposes."""

from .config import SCREEN_HEIGHT, SCREEN_WIDTH, TARGET_FPS
from .main import run_game

__all__ = ["run_game", "SCREEN_WIDTH", "SCREEN_HEIGHT", "TARGET_FPS"]
