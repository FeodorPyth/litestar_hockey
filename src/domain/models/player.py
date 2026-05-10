from __future__ import annotations
from typing import TYPE_CHECKING
import msgspec
from enum import StrEnum

from lib.schema import CamelizedBaseStruct

if TYPE_CHECKING:
    from domain.models.team import Team


class StickGrip(StrEnum):
    LEFT = "left"
    RIGHT = "right"


class Player(CamelizedBaseStruct):
    name: str
    surname: str

    # in centimeters
    height: int
    # in kilograms
    weight: int

    number: int
    stick_grip: StickGrip

    team: Team | None = None


class PlayerCreate(CamelizedBaseStruct):
    name: str
    surname: str

    height: int
    weight: int

    number: int
    stick_grip: StickGrip

    team_name: str | msgspec.UnsetType | None = msgspec.UNSET

    def __post_init__(self):
        if not 1 <= self.height <= 300:
            raise ValueError("Height must be between 1 and 300 cm")
        if not 1 <= self.weight <= 200:
            raise ValueError("Weight must be between 1 and 200 kg")
        if not 0 <= self.number <= 99:
            raise ValueError("Number must be between 0 and 99")


class PlayerUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    surname: str | msgspec.UnsetType | None = msgspec.UNSET

    height: int | msgspec.UnsetType | None = msgspec.UNSET
    weight: int | msgspec.UnsetType | None = msgspec.UNSET

    number: int | msgspec.UnsetType | None = msgspec.UNSET
    stick_grip: StickGrip | msgspec.UnsetType | None = msgspec.UNSET

    team_name: str | msgspec.UnsetType | None = msgspec.UNSET
