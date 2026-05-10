"""init base models

Revision ID: 01
Revises:
Create Date: 2026-05-02 14:05:51.340216

"""

import warnings
from typing import Any

import sqlalchemy as sa
from alembic import op
from advanced_alchemy.types import (
    EncryptedString,
    EncryptedText,
    GUID,
    ORA_JSONB,
    DateTimeUTC,
    StoredObject,
    PasswordHash,
    FernetBackend,
)
from advanced_alchemy.types.encrypted_string import PGCryptoBackend
from sqlalchemy import Text  # noqa: F401

try:
    from advanced_alchemy.types.password_hash.argon2 import Argon2Hasher
except ImportError:
    Argon2Hasher = Any  # type: ignore
try:
    from advanced_alchemy.types.password_hash.passlib import PasslibHasher
except ImportError:
    PasslibHasher = Any  # type: ignore
try:
    from advanced_alchemy.types.password_hash.pwdlib import PwdlibHasher
except ImportError:
    PwdlibHasher = Any  # type: ignore

__all__ = ["downgrade", "upgrade", "schema_upgrades", "schema_downgrades", "data_upgrades", "data_downgrades"]

sa.GUID = GUID
sa.DateTimeUTC = DateTimeUTC
sa.ORA_JSONB = ORA_JSONB
sa.EncryptedString = EncryptedString
sa.EncryptedText = EncryptedText
sa.StoredObject = StoredObject
sa.PasswordHash = PasswordHash
sa.Argon2Hasher = Argon2Hasher
sa.PasslibHasher = PasslibHasher
sa.PwdlibHasher = PwdlibHasher
sa.FernetBackend = FernetBackend
sa.PGCryptoBackend = PGCryptoBackend

# revision identifiers, used by Alembic.
revision = "01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            schema_upgrades()
            data_upgrades()


def downgrade() -> None:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        with op.get_context().autocommit_block():
            data_downgrades()
            schema_downgrades()


def schema_upgrades() -> None:
    """schema upgrade migrations go here."""
    op.create_table(
        "cities",
        sa.Column("id", sa.GUID(length=16), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("district", sa.String(), nullable=False),
        sa.Column("sa_orm_sentinel", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_cities")),
        sa.UniqueConstraint("name", "district", name="unique_city_per_district"),
    )
    with op.batch_alter_table("cities", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_cities_name"), ["name"], unique=True)

    op.create_table(
        "stadiums",
        sa.Column("id", sa.GUID(length=16), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("city_id", sa.GUID(length=16), nullable=False),
        sa.Column("sa_orm_sentinel", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["city_id"], ["cities.id"], name=op.f("fk_stadiums_city_id_cities"), ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_stadiums")),
        sa.UniqueConstraint("name", "city_id", name="unique_stadium_per_city"),
    )
    with op.batch_alter_table("stadiums", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_stadiums_name"), ["name"], unique=False)

    op.create_table(
        "teams",
        sa.Column("id", sa.GUID(length=16), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("city_id", sa.GUID(length=16), nullable=False),
        sa.Column("stadium_id", sa.GUID(length=16), nullable=False),
        sa.Column("sa_orm_sentinel", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["city_id"], ["cities.id"], name=op.f("fk_teams_city_id_cities"), ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["stadium_id"], ["stadiums.id"], name=op.f("fk_teams_stadium_id_stadiums"), ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_teams")),
    )
    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_teams_name"), ["name"], unique=True)

    op.create_table(
        "coaches",
        sa.Column("id", sa.GUID(length=16), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("is_head_coach", sa.Boolean(), server_default=sa.text("false"), nullable=False),
        sa.Column("team_id", sa.GUID(length=16), nullable=True),
        sa.Column("sa_orm_sentinel", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"], name=op.f("fk_coaches_team_id_teams"), ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_coaches")),
    )
    with op.batch_alter_table("coaches", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_coaches_surname"), ["surname"], unique=False)
        batch_op.create_index(
            "unique_head_coach_per_team", ["team_id"], unique=True, postgresql_where=sa.text("is_head_coach IS TRUE")
        )

    op.create_table(
        "players",
        sa.Column("id", sa.GUID(length=16), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("surname", sa.String(), nullable=False),
        sa.Column("height", sa.Integer(), nullable=False, comment="Height in cm"),
        sa.Column("weight", sa.Integer(), nullable=False, comment="Weight in kg"),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("stick_grip", sa.String(), nullable=False),
        sa.Column("team_id", sa.GUID(length=16), nullable=True),
        sa.Column("sa_orm_sentinel", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTimeUTC(timezone=True), nullable=False),
        sa.CheckConstraint("height > 0 AND height < 300", name=op.f("ck_players_check_height")),
        sa.CheckConstraint("weight > 0 AND weight < 200", name=op.f("ck_players_check_weight")),
        sa.ForeignKeyConstraint(["team_id"], ["teams.id"], name=op.f("fk_players_team_id_teams"), ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_players")),
        sa.UniqueConstraint("number", "team_id", name="unique_number_per_team"),
    )
    with op.batch_alter_table("players", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_players_surname"), ["surname"], unique=False)


def schema_downgrades() -> None:
    """schema downgrade migrations go here."""
    with op.batch_alter_table("players", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_players_surname"))

    op.drop_table("players")
    with op.batch_alter_table("coaches", schema=None) as batch_op:
        batch_op.drop_index("unique_head_coach_per_team", postgresql_where=sa.text("is_head_coach IS TRUE"))
        batch_op.drop_index(batch_op.f("ix_coaches_surname"))

    op.drop_table("coaches")
    with op.batch_alter_table("teams", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_teams_name"))

    op.drop_table("teams")
    with op.batch_alter_table("stadiums", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_stadiums_name"))

    op.drop_table("stadiums")
    with op.batch_alter_table("cities", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_cities_name"))

    op.drop_table("cities")


def data_upgrades() -> None:
    """Add any optional data upgrade migrations here!"""


def data_downgrades() -> None:
    """Add any optional data downgrade migrations here!"""
