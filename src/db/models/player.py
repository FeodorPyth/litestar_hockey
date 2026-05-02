from __future__ import annotations
from typing import TYPE_CHECKING

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

if TYPE_CHECKING:
    from src.db.models.team import Team


class Player(base.UUIDv7AuditBase):
    __tablename__ = "players"

    __table_args__ = (
        UniqueConstraint("number", "team_id", name="unique_number_per_team"),
        CheckConstraint("height > 0 AND height < 300", name="check_height"),
        CheckConstraint("weight > 0 AND weight < 200", name="check_weight"),
    )

    name: Mapped[str]
    surname: Mapped[str] = mapped_column(index=True)

    height: Mapped[int] = mapped_column(comment="Height in cm")
    weight: Mapped[int] = mapped_column(comment="Weight in kg")

    number: Mapped[int]
    stick_grip: Mapped[str]

    team_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True,
        default=None,
    )
    team: Mapped[Team | None] = relationship(back_populates="players")
