from typing import Optional, List

from pydantic import BaseModel, ConfigDict, HttpUrl


class ServiceBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str]
    url: Optional[HttpUrl]


class ServiceCreate(ServiceBase):
    password: str


class ServiceRead(ServiceBase):
    id: int
    user_id: int

    owner: Optional["UserRead"] = None
    passwords: Optional[List["PasswordRead"]] = None


class ServiceUpdate(ServiceRead):
    pass
