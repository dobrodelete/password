from typing import Optional

from sqlalchemy import insert

from app.crud import BaseCrud
from app.models import User
from app.schemas import UserCreate, UserRead


class Create(BaseCrud):
    def __init__(self):
        super().__init__()

    async def create_user(self, user: UserCreate) -> Optional[UserRead]:
        async with self.insert_session_scope() as s:
            result = s.execute(insert(User).values(

            ))
