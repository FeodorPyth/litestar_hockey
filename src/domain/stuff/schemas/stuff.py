from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class Coach(CamelizedBaseStruct):
    name: str
    surname: str

    is_head_coach: bool =  False

    team: Team
