# """All configuration via environment.

# Take note of the environment variable prefixes required for each
# settings class, except `AppSettings`.
# """

# from __future__ import annotations

# import binascii
# import json
# import logging
# import os
# import sys
# from dataclasses import dataclass, field
# from functools import lru_cache
# from pathlib import Path
# from typing import TYPE_CHECKING, Final, cast

# import structlog
# from advanced_alchemy.extensions.litestar import AlembicAsyncConfig, AsyncSessionConfig, SQLAlchemyAsyncConfig
# from advanced_alchemy.utils.text import slugify
# from dotenv import load_dotenv
# from litestar.cli._utils import console
# from litestar.config.compression import CompressionConfig
# from litestar.config.cors import CORSConfig
# from litestar.data_extractors import RequestExtractorField, ResponseExtractorField
# from litestar.exceptions import NotAuthorizedException, PermissionDeniedException
# from litestar.logging.config import LoggingConfig, StructLoggingConfig, default_logger_factory
# from litestar.middleware.logging import LoggingMiddlewareConfig
# from litestar.plugins.problem_details import ProblemDetailsConfig
# from litestar.plugins.structlog import StructlogConfig
# from litestar.utils.module_loader import module_to_os_path

# from app.__metadata__ import __version__ as current_version
# from app.utils.env import get_env

# if TYPE_CHECKING:
#     from sqlalchemy.ext.asyncio import AsyncEngine

# DEFAULT_MODULE_NAME = "src"
# BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)


# @dataclass
# class DatabaseSettings:
#     ECHO: bool = field(default_factory=get_env("DATABASE_ECHO", False))
#     """Enable SQLAlchemy engine logs."""
#     ECHO_POOL: bool = field(default_factory=get_env("DATABASE_ECHO_POOL", False))
#     """Enable SQLAlchemy connection pool logs."""
#     POOL_DISABLED: bool = field(default_factory=get_env("DATABASE_POOL_DISABLED", False))
#     """Disable SQLAlchemy pool configuration."""
#     POOL_MAX_OVERFLOW: int = field(default_factory=get_env("DATABASE_MAX_POOL_OVERFLOW", 10))
#     """Max overflow for SQLAlchemy connection pool"""
#     POOL_SIZE: int = field(default_factory=get_env("DATABASE_POOL_SIZE", 5))
#     """Pool size for SQLAlchemy connection pool"""
#     POOL_TIMEOUT: int = field(default_factory=get_env("DATABASE_POOL_TIMEOUT", 30))
#     """Time in seconds for timing connections out of the connection pool."""
#     POOL_RECYCLE: int = field(default_factory=get_env("DATABASE_POOL_RECYCLE", 300))
#     """Amount of time to wait before recycling connections."""
#     POOL_PRE_PING: bool = field(default_factory=get_env("DATABASE_PRE_POOL_PING", False))
#     """Optionally ping database before fetching a session from the connection pool."""
#     URL: str = field(default_factory=get_env("DATABASE_URL", "postgresql+psycopg://app:app@localhost:15432/app"))
#     """SQLAlchemy Database URL."""
#     MIGRATION_CONFIG: str = field(
#         default_factory=get_env("DATABASE_MIGRATION_CONFIG", f"{BASE_DIR}/db/migrations/alembic.ini")
#     )
#     """The path to the `alembic.ini` configuration file."""
#     MIGRATION_PATH: str = field(default_factory=get_env("DATABASE_MIGRATION_PATH", f"{BASE_DIR}/db/migrations"))
#     """The path to the `alembic` database migrations."""
#     MIGRATION_DDL_VERSION_TABLE: str = field(
#         default_factory=get_env("DATABASE_MIGRATION_DDL_VERSION_TABLE", "ddl_version")
#     )
#     """The name to use for the `alembic` versions table name."""
#     FIXTURE_PATH: str = field(default_factory=get_env("DATABASE_FIXTURE_PATH", f"{BASE_DIR}/db/fixtures"))
#     """The path to JSON fixture files to load into tables."""
#     _engine_instance: AsyncEngine | None = None
#     """SQLAlchemy engine instance generated from settings."""

#     @property
#     def engine(self) -> AsyncEngine:
#         return self.get_engine()

#     def get_engine(self) -> AsyncEngine:
#         if self._engine_instance is not None:
#             return self._engine_instance
#         from app.utils.engine_factory import create_sqlalchemy_engine

#         self._engine_instance = create_sqlalchemy_engine(self)
#         return self._engine_instance

#     def get_config(self) -> SQLAlchemyAsyncConfig:
#         """Get SQLAlchemy configuration.

#         Returns:
#             The SQLAlchemy async configuration.
#         """
#         return SQLAlchemyAsyncConfig(
#             engine_instance=self.get_engine(),
#             before_send_handler="autocommit",
#             session_config=AsyncSessionConfig(expire_on_commit=False),
#             alembic_config=AlembicAsyncConfig(
#                 version_table_name=self.MIGRATION_DDL_VERSION_TABLE,
#                 script_config=self.MIGRATION_CONFIG,
#                 script_location=self.MIGRATION_PATH,
#             ),
#         )

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки базы данных"""

    # PostgreSQL
    DB_HOST: str = "localhost"
    DB_PORT: int = 5433
    DB_USER: str = "hockeysmash_user"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "hockeysmash"
    DB_DRIVER: str = "asyncpg"

    @property
    def url(self) -> str:
        return f"postgresql+{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class AppSettings(BaseSettings):
    """Основные настройки приложения"""

    APP_NAME: str = "HockeySmash API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Подгруппы настроек
    database: DatabaseSettings = DatabaseSettings()

    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = AppSettings()
