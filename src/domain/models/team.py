from __future__ import annotations
from typing import TYPE_CHECKING
import msgspec

from lib.schema import CamelizedBaseStruct

if TYPE_CHECKING:
    from domain.models.city import City
    from domain.models.player import Player
    from domain.models.stadium import Stadium
    from domain.models.stuff import Coach


class Team(CamelizedBaseStruct):
    name: str

    city: City
    stadium: Stadium
    players: list[Player] | None = None
    coaches: list[Coach] | None = None


class TeamCreate(CamelizedBaseStruct):
    name: str

    city_name: str
    stadium_name: str


class TeamUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET

    city_name: str | msgspec.UnsetType | None = msgspec.UNSET
    stadium_name: str | msgspec.UnsetType | None = msgspec.UNSET
