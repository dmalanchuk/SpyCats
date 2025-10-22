from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from src.database import Base
from src.models.missions_model import MissionsModel


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
