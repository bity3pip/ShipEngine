import os

from arq import create_pool
from arq.connections import RedisSettings
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost/{os.getenv('POSTGRES_DB')}"
)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session

async def get_arq_pool():
    redis_host = os.getenv("REDIS_HOST", "redis")
    redis_port = os.getenv("REDIS_PORT", 6379)
    return await create_pool(RedisSettings(host=redis_host, port=redis_port))
