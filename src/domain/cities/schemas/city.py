import msgspec

from src.domain.stadiums.schemas import Stadium
from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class City(CamelizedBaseStruct):
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
