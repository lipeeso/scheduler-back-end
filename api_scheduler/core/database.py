from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from api_scheduler.core.settings import Settings

settings = Settings()

engine = create_async_engine(settings.DATABASE_URL)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session