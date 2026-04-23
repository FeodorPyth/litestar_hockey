from litestar import Litestar, get
from litestar.openapi import OpenAPIConfig


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/players/{player_id:str}")
async def get_book(player_id: str) -> dict[str, str]:
    return {"player_id": player_id}


app = Litestar(
    [index, get_book],
    openapi_config=OpenAPIConfig(
        title="My API",
        version="1.0.0",
        use_cdn=False,  # Принудительно использовать локальные файлы
    ),
)
