from litestar import Router

from .city import CityController
from .stadium import StadiumController

base_router = Router(
    path="/api/v1",
    route_handlers=[
        CityController,
        StadiumController,
    ]
)
