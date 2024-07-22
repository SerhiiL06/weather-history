import os
from collections.abc import AsyncGenerator

from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from src.infrastructure.settings import config


class DatabaseCORE:
    def __init__(
        self, db_name: str, username: str, password: str, host: str, port: str
    ) -> None:
        self._DB_NAME = db_name
        self._DB_USERNAME = username
        self._DB_PASSWORD = password
        self._DB_HOST = host
        self._DB_PORT = port

    @property
    def _db_url(self):
        url = URL.create(
            drivername="postgresql+asyncpg",
            username=self._DB_USERNAME,
            password=self._DB_PASSWORD,
            host=self._DB_HOST,
            port=self._DB_PORT,
            database=self._DB_NAME,
        )
        return url

    @property
    def _engine(self):
        return create_async_engine(
            self._db_url, echo=True, pool_size=10, max_overflow=5
        )

    @property
    def session_factory(self) -> async_sessionmaker:
        return async_sessionmaker(self._engine, class_=AsyncSession, autoflush=False)


core = DatabaseCORE(
    config.db_name,
    config.db_username,
    config.db_password,
    config.db_host,
    config.db_port,
)


async def session_transaction() -> AsyncGenerator:
    async with core.session_factory() as conn:
        yield conn
