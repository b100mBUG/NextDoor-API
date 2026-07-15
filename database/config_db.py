from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv(".env")


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///nextdoor.db")


engine = create_async_engine(
    DATABASE_URL,
    echo=False
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session():
    async with async_session() as session:
        yield session


