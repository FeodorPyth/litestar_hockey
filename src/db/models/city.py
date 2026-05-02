from __future__ import annotations
from typing import TYPE_CHECKING

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, mapped_column

if TYPE_CHECKING:
    from src.db.models.stadium import Stadium
    from src.db.models.team import Team


class City(base.UUIDv7AuditBase):
    __tablename__ = "cities"

    __table_args__ = (UniqueConstraint("name", "district", name="unique_city_per_district"),)

    name: Mapped[str] = mapped_column(unique=True, index=True)
    district: Mapped[str]

    stadiums: Mapped[list[Stadium]] = relationship(
        back_populates="city",
        lazy="selectin",
        passive_deletes=True,
    )
    teams: Mapped[list[Team]] = relationship(
        back_populates="city",
        lazy="selectin",
        passive_deletes=True,
    )
