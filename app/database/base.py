from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from app.config_loader import load_config

from .config import DBConfig


class Base(DeclarativeBase):
    pass


db_config = load_config(DBConfig, "database")


def build_sa_engine() -> AsyncEngine:
    engine = create_async_engine(db_config.full_url, echo=True)
    return engine


def build_sa_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return session_factory
