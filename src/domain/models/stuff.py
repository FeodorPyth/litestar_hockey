from __future__ import annotations
from typing import TYPE_CHECKING
import msgspec

from lib.schema import CamelizedBaseStruct

if TYPE_CHECKING:
    from domain.models.team import Team


class Coach(CamelizedBaseStruct):
    name: str
    surname: str

    is_head_coach: bool = False

    team: Team | None = None


class CoachCreate(CamelizedBaseStruct):
    name: str
    surname: str

    is_head_coach: bool = False

    team_name: str | None = None


class CoachUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    surname: str | msgspec.UnsetType | None = msgspec.UNSET

    is_head_coach: bool | msgspec.UnsetType | None = msgspec.UNSET

    team_name: str | msgspec.UnsetType | None = msgspec.UNSET
