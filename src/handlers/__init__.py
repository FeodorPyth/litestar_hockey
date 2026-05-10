from litestar import Router

from .city import CityController

base_router = Router(path="/api/v1", route_handlers=[CityController])
