from typing import List

from sqlalchemy import DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.utils.security import encrypt_password, decrypt_password


class Password(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    encrypted_password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    account_name: Mapped[str] = mapped_column(nullable=True)
    service_id: Mapped[int] = mapped_column(ForeignKey('services.id'), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    owner: Mapped['User'] = relationship("User", back_populates="passwords")
    service: Mapped['Service'] = relationship("Service", back_populates="passwords")

    def encrypt_password(self, plaintext_password: str, master_password: str):
        self.encrypted_password = encrypt_password(plaintext_password, master_password)

    def decrypt_password(self, master_password: str) -> str:
        return decrypt_password(self._encrypted_password, master_password)
