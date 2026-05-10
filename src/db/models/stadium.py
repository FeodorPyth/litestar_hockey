from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import UUID

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from src.db.models.city import City
    from src.db.models.team import Team


class Stadium(base.UUIDv7AuditBase):
    __tablename__ = "stadiums"

    __table_args__ = (UniqueConstraint("name", "city_id", name="unique_stadium_per_city"),)

    name: Mapped[str] = mapped_column(index=True)

    image_path: Mapped[str | None] = mapped_column(String(500), nullable=True, default=None)

    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id", ondelete="CASCADE"))
    city: Mapped[City] = relationship(back_populates="stadiums")
    teams: Mapped[list[Team]] = relationship(
        back_populates="stadium",
        lazy="selectin",
    )
