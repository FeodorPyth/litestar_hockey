from pathlib import Path

from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)
from advanced_alchemy.config import AlembicAsyncConfig

from src.lib.settings import settings

session_config = AsyncSessionConfig(expire_on_commit=False)
alchemy_config = SQLAlchemyAsyncConfig(
    connection_string=settings.database.url,
    alembic_config=AlembicAsyncConfig(script_location=str(Path(__file__).parent / "migrations")),
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=alchemy_config)
