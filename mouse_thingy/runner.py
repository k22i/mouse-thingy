from __future__ import annotations

import json
import logging
import random
import time
from pathlib import Path

from .actions import perform_click, perform_keypress, perform_scroll
from .config import Config, ClickAction, ScrollAction

logger = logging.getLogger(__name__)


def load_config(config_path: Path) -> Config:
    raw = json.loads(config_path.read_text(encoding="utf-8"))
    return Config.model_validate(raw)


def run_actions(config: Config) -> None:
    min_delay, max_delay = config.delay_between_actions_range
    should_repeat = config.repeat
    while True:
        for action in config.actions:
            if isinstance(action, ClickAction):
                logger.info("Click: %s", action)
                perform_click(action)
            elif isinstance(action, ScrollAction):
                logger.info("Scroll: %s", action)
                perform_scroll(action)
            else:
                logger.info("Keypress: %s", action)
                perform_keypress(action)

            delay = random.uniform(min_delay, max_delay)
            logger.info("Sleeping %.2f seconds", delay)
            time.sleep(delay)

        if not should_repeat:
            break
