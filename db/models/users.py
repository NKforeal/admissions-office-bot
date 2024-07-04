from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import types
from db.database import Base
from datetime import date


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    tg_id: Mapped[int] = mapped_column(types.BIGINT, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True, unique=True)
    creation_date: Mapped[date] = mapped_column(nullable=False)
    queue_number: Mapped[int] = mapped_column(nullable=False, default=False)
