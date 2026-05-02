from __future__ import annotations
from typing import TYPE_CHECKING

from advanced_alchemy.extensions.litestar import base
from sqlalchemy import ForeignKey, Index, false, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

if TYPE_CHECKING:
    from src.db.models.team import Team


class Coach(base.UUIDv7AuditBase):
    __tablename__ = "coaches"

    __table_args__ = (
        Index(
            "unique_head_coach_per_team",
            "team_id",
            unique=True,
            postgresql_where=(
                text("is_head_coach IS TRUE")
            ),
        ),
    )

    name: Mapped[str]
    surname: Mapped[str] = mapped_column(index=True)

    is_head_coach: Mapped[bool] = mapped_column(default=False, server_default=false())
    team_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True,
        default=None,
    )
    team: Mapped[Team | None] = relationship(back_populates="coaches")
