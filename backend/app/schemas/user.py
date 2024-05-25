from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    hashed_password: str
    is_active: bool = True

    passwords: Optional[List["PasswordRead"]] = None
    services: Optional[List["ServiceRead"]] = None


class UserUpdate(UserRead):
    pass
