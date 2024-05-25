from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext

from app.database import db_helper

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class BaseCrud:
    def __init__(self) -> None:
        self.session = db_helper.session_factory

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)

    @asynccontextmanager
    async def insert_session_scope(self) -> None:
        async with self.session.begin() as s:
            try:
                yield s
                await s.commit()
            except SQLAlchemyError as e:
                print(e)
                await s.rollback()
                raise
            finally:
                await s.close()

    @asynccontextmanager
    async def read_session_scope(self) -> None:
        async with self.session.begin() as s:
            try:
                yield s
            except SQLAlchemyError as e:
                print(e)
                raise
            finally:
                await s.close()
