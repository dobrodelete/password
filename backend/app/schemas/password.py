from typing import Optional

from pydantic import BaseModel, ConfigDict


class PasswordBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    encrypted_password: str
    name: Optional[str] = None
    description: Optional[str] = None
    account_name: Optional[str] = None


class PasswordCreate(PasswordBase):
    password: str
    service_id: Optional[int] = None
    master_password: str


class PasswordRead(PasswordBase):
    id: int
    encrypted_password: str
    service_id: Optional[int]
    user_id: int

    owner: Optional["UserRead"] = None
    service: Optional["ServiceRead"] = None


class PasswordUpdate(PasswordRead):
    pass
