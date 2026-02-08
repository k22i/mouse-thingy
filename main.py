from __future__ import annotations

import argparse
import logging
from pathlib import Path

from mouse_thingy.runner import load_config, run_actions


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Automatic mouse/keyboard action runner")
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=Path(__file__).resolve().parent / "config.json",
        help="Path to the config JSON file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    config = load_config(args.config)
    run_actions(config)


if __name__ == "__main__":
    main()
