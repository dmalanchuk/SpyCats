from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class MessageModel(Base):
    __tablename__ = "spy_cats"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    breed: Mapped[str] = mapped_column(nullable=False)
    salary: Mapped[int] = mapped_column(nullable=False)
