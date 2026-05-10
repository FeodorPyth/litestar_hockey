"""add to models image_path

Revision ID: 02
Revises: 01
Create Date: 2026-05-10 14:49:19.305906

"""

import warnings
from typing import TYPE_CHECKING, Any

import sqlalchemy as sa
from alembic import op
from advanced_alchemy.types import EncryptedString, EncryptedText, GUID, ORA_JSONB, DateTimeUTC, StoredObject, PasswordHash, FernetBackend
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

if TYPE_CHECKING:
    from collections.abc import Sequence

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
revision = '02'
down_revision = '01'
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
    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=500), nullable=True))

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=500), nullable=True))

    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=500), nullable=True))

    with op.batch_alter_table('stadiums', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=500), nullable=True))

    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=500), nullable=True))


def schema_downgrades() -> None:
    """schema downgrade migrations go here."""
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('stadiums', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('players', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('coaches', schema=None) as batch_op:
        batch_op.drop_column('image_path')

    with op.batch_alter_table('cities', schema=None) as batch_op:
        batch_op.drop_column('image_path')


def data_upgrades() -> None:
    """Add any optional data upgrade migrations here!"""

def data_downgrades() -> None:
    """Add any optional data downgrade migrations here!"""
