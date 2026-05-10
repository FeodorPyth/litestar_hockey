from .city import City, CityCreate, CityUpdate
from .player import Player, PlayerCreate, PlayerUpdate
from .stadium import Stadium, StadiumCreate, StadiumUpdate
from .stuff import Coach, CoachCreate, CoachUpdate
from .team import Team, TeamCreate, TeamUpdate

import domain.models.city as _city
import domain.models.stadium as _stadium
import domain.models.team as _team
import domain.models.player as _player
import domain.models.stuff as _stuff

_city.Stadium = Stadium
_city.Team = Team

_stadium.City = City
_stadium.Team = Team

_team.City = City
_team.Player = Player
_team.Stadium = Stadium
_team.Coach = Coach

_player.Team = Team

_stuff.Team = Team

__all__ = (
    "City",
    "CityCreate",
    "CityUpdate",
    "Player",
    "PlayerCreate",
    "PlayerUpdate",
    "Stadium",
    "StadiumCreate",
    "StadiumUpdate",
    "Coach",
    "CoachCreate",
    "CoachUpdate",
    "Team",
    "TeamCreate",
    "TeamUpdate",
)
