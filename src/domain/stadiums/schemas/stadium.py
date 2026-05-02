import msgspec

from src.domain.cities.schemas import City
from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class Stadium(CamelizedBaseStruct):
    name: str

    city: City
    teams: list[Team] | None = None


class StadiumCreate(CamelizedBaseStruct):
    name: str
    city: str


class StadiumUpdate(CamelizedBaseStruct, omit_defaults=True):
    name: str | msgspec.UnsetType | None = msgspec.UNSET
    city: str | msgspec.UnsetType | None = msgspec.UNSET
