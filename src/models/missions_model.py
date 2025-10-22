from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class MessageModel(Base):
    __tablename__ = "missions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cats: Mapped[int] = mapped_column(nullable=False)

