from typing import Optional

from sqlalchemy import select

from app.crud import BaseCrud
from app.models import User
from app.schemas import UserRead


class Read(BaseCrud):
    def __init__(self):
        super().__init__()

    async def get_user_by_email(self, email: str) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(User).where(User.email == email)
            )
            user = result.scalar()
            return UserRead.model_validate(user) if user else None

