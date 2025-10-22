from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from src.database import Base


class CatsModel(Base):
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    years_of_experience: Mapped[int] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False)

    salary: Mapped[int] = mapped_column(nullable=False)

    mission_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('missions.id', ondelete="SET NULL"),
        nullable=True,
        unique=True
    )

    mission: Mapped[Optional["MissionsModel"]] = relationship(
        back_populates="cat",
        uselist=False
    )

    class MissionsModel(Base):
        __tablename__ = "missions"

        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        is_complete: Mapped[bool] = mapped_column(nullable=False, default=False)

        cat: Mapped[Optional["CatsModel"]] = relationship(
            back_populates="mission",
            uselist=False
        )

        targets: Mapped[list["TargetsModel"]] = relationship(
            back_populates="mission",
            cascade="all, delete-orphan"
        )


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
