import msgspec

from src.domain.cities.schemas import City
from src.domain.players.schemas import Player
from src.domain.stadiums.schemas import Stadium
from src.domain.stuff.schemas import Coach
from src.lib.schema import CamelizedBaseStruct


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
