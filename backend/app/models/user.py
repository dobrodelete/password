from typing import List

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base


class User(Base):
    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, autoincrement=False, index=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

    passwords: Mapped[List["Password"]] = relationship(back_populates="user")
    services: Mapped[List['Service']] = relationship(back_populates="owner")
