from src.domain.cities.schemas import City
from src.domain.players.schemas import Player
from src.domain.stadiums.schemas import Stadium
from src.domain.stuff.schemas import Coach
from src.lib.schema import CamelizedBaseStruct


class Team(CamelizedBaseStruct):
    name: str
    
    city: City
    stadium: Stadium
    players: list[Player]
    coaches: list[Coach]
