from src.database import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UniqueConstraint


class TargetsModel(Base):
    __tablename__ = "targets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mission_id: Mapped[int] = mapped_column(ForeignKey("missions.id"))
    name: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(default="")
    status: Mapped[str] = mapped_column(nullable=False, default="Not Started")

    mission: Mapped["MissionsModel"] = relationship(back_populates="targets")

    __table_args__ = (
        UniqueConstraint('mission_id', 'name', name='uq_mission_target_name'),
    )