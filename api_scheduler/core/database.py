from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine



engine = create_async_engine(

)

async def get_session():
    async with AsyncSession(engine) as session:
        yield session