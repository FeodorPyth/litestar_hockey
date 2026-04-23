from src.domain.teams.schemas import Team
from src.lib.schema import CamelizedBaseStruct


class Player(CamelizedBaseStruct):
    name: str
    surname: str

    # in centimeters
    height: int
    # in kilograms
    weight: int

    number: int
    stick_grip: str

    team: Team
