from src.domain.stadiums.schemas import Stadium
from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class City(CamelizedBaseStruct):
    name: str
    district: str

    stadiums: list[Stadium] | None = None
    teams: list[Team] | None = None
