from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import UUID
import msgspec

from lib.schema import CamelizedBaseStruct

if TYPE_CHECKING:
    from domain.models.city import City
    from domain.models.team import Team


class Stadium(CamelizedBaseStruct):
    id: UUID

    name: str

    city: City
    teams: list[Team] | None = None


class StadiumCreate(CamelizedBaseStruct):
    name: str
    city_id: UUID


class StadiumUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    city_id: UUID | msgspec.UnsetType | None = msgspec.UNSET
