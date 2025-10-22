from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from typing import Optional


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
