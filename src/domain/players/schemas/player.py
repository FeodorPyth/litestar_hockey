import msgspec
from enum import StrEnum

from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


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

    height: int = msgspec.field(ge=1, le=300)
    weight: int = msgspec.field(ge=1, le=200)

    number: int
    stick_grip: StickGrip

    team_name: str | msgspec.UnsetType | None = msgspec.UNSET


class PlayerUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    surname: str | msgspec.UnsetType | None = msgspec.UNSET

    height: int | msgspec.UnsetType | None = msgspec.UNSET
    weight: int | msgspec.UnsetType | None = msgspec.UNSET

    number: int | msgspec.UnsetType | None = msgspec.UNSET
    stick_grip: StickGrip | msgspec.UnsetType | None = msgspec.UNSET

    team_name: str | msgspec.UnsetType | None = msgspec.UNSET
