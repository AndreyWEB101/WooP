from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

DATABASE_URL="postgresql+asyncpg://andrey@localhost:5432/WooP_db"
async_engine_db=create_async_engine(DATABASE_URL,echo=True)
async_session_loacal=async_sessionmaker(bind=async_engine_db,class_=AsyncSession,expire_on_commit=False)


async def get_db():
    async with async_session_loacal() as session:
        yield session


