from src.domain.cities.schemas import City
from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class Stadium(CamelizedBaseStruct):
    name: str

    city: City
    team: list[Team] | None = None
