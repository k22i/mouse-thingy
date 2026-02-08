from __future__ import annotations

import logging
import time
from typing import Set

import pyautogui
import pyperclip
from pynput import keyboard


def _format_coords() -> str:
    x, y = pyautogui.position()
    return f"[{x}, {y}]"


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logger = logging.getLogger("coordinate_getter")

    pressed: Set[keyboard.Key | keyboard.KeyCode] = set()
    combo = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode.from_char("c")}

    def on_press(key: keyboard.Key | keyboard.KeyCode) -> None:
        pressed.add(key)
        if combo.issubset(pressed):
            coords = _format_coords()
            pyperclip.copy(coords)
            logger.info("Copied cursor coordinates to clipboard: %s", coords)
            time.sleep(0.2)

    def on_release(key: keyboard.Key | keyboard.KeyCode) -> None:
        pressed.discard(key)

    logger.info("Press Ctrl+Shift+C to copy cursor coordinates.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
