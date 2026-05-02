from __future__ import annotations
from typing import TYPE_CHECKING

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

if TYPE_CHECKING:
    from src.db.models.city import City
    from src.db.models.player import Player
    from src.db.models.stadium import Stadium
    from src.db.models.stuff import Coach


class Team(base.UUIDv7AuditBase):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(unique=True, index=True)

    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id", ondelete="CASCADE"))
    city: Mapped[City] = relationship(back_populates="teams")

    players: Mapped[list[Player]] = relationship(
        back_populates="team",
        lazy="selectin",
    )

    stadium_id: Mapped[UUID] = mapped_column(ForeignKey("stadiums.id", ondelete="CASCADE"))
    stadium: Mapped[Stadium] = relationship(back_populates="teams")

    coaches: Mapped[list[Coach]] = relationship(
        back_populates="team",
        lazy="selectin",
    )
