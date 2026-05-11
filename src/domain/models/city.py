from __future__ import annotations
from typing import TYPE_CHECKING
import msgspec

from uuid import UUID

from lib.schema import CamelizedBaseStruct

if TYPE_CHECKING:
    from domain.models.stadium import Stadium
    from domain.models.team import Team


class City(CamelizedBaseStruct):
    id: UUID

    name: str
    district: str

    stadiums: list[Stadium] | None = None
    teams: list[Team] | None = None


class CityCreate(CamelizedBaseStruct):
    name: str
    district: str


class CityUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    district: str | msgspec.UnsetType | None = msgspec.UNSET
