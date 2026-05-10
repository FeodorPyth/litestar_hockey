from pathlib import Path

from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from litestar.static_files import create_static_files_router

from db.base import alchemy
from handlers import base_router

static_router = create_static_files_router(
    path="/static",
    directories=[Path("uploads")],
    name="static",
)

app = Litestar(
    route_handlers=[static_router, base_router],
    openapi_config=OpenAPIConfig(
        title="My API",
        version="1.0.0",
    ),
    plugins=[alchemy],
    debug=True,
)
