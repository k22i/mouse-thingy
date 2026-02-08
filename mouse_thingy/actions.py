from __future__ import annotations

import time
from typing import Final

import pyautogui

from .config import ClickAction, ScrollAction, KeypressAction


_KEY_ALIASES: Final[dict[str, str]] = {
    "spacebar": "space",
    "esc": "esc",
    "escape": "esc",
    "enter": "enter",
    "return": "enter",
    "tab": "tab",
}


def _normalize_key(key: str) -> str:
    return _KEY_ALIASES.get(key.lower(), key)


def perform_click(action: ClickAction) -> None:
    x, y = action.coordinates
    pyautogui.click(x=x, y=y, button=action.button)


def perform_scroll(action: ScrollAction) -> None:
    x, y = action.coordinates
    amount = action.scroll_config.scroll_length
    if action.scroll_config.direction == "down":
        amount = -amount
    pyautogui.scroll(amount, x=x, y=y)


def perform_keypress(action: KeypressAction) -> None:
    key = _normalize_key(action.key)
    pyautogui.keyDown(key)
    time.sleep(action.press_down_duration)
    pyautogui.keyUp(key)
