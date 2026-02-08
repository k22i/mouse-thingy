from __future__ import annotations

from typing import Literal, Annotated

from pydantic import BaseModel, Field, PositiveInt, PositiveFloat, field_validator


class ClickAction(BaseModel):
    type: Literal["click"]
    coordinates: tuple[int, int]
    button: Literal["left", "right", "middle"] = "left"


class ScrollConfig(BaseModel):
    direction: Literal["up", "down"]
    scroll_length: PositiveInt = 200


class ScrollAction(BaseModel):
    type: Literal["scroll"]
    coordinates: tuple[int, int]
    scroll_config: ScrollConfig


class KeypressAction(BaseModel):
    type: Literal["keypress"]
    key: str
    press_down_duration: PositiveFloat = 0.1


Action = ClickAction | ScrollAction | KeypressAction


class Config(BaseModel):
    delay_between_actions_range: tuple[PositiveFloat, PositiveFloat] = (1.0, 5.0)
    actions: list[Annotated[Action, Field(discriminator="type")]] = Field(
        default_factory=list
    )
    repeat: bool = False

    @field_validator("delay_between_actions_range")
    @classmethod
    def _validate_delay_range(cls, value: tuple[float, float]) -> tuple[float, float]:
        min_delay, max_delay = value
        if min_delay > max_delay:
            raise ValueError("delay_between_actions_range must be [min, max]")
        return value
