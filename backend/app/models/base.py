from sqlalchemy import func, DateTime
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped


class Base(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    @declared_attr.directive
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    def __str__(self) -> str:
        columns_str = ", ".join(
            [
                f"{column.name}={getattr(self, column.name)!r}"
                for column in self.__table__.columns
            ]
        )
        return f"{self.__class__.__name__}({columns_str})"

    def __perp__(self) -> str:
        columns_str = ", ".join(
            [
                f"{column.name}={getattr(self, column.name)!r}"
                for column in self.__table__.columns
            ]
        )
        return f"{self.__class__.__name__}({columns_str})"
