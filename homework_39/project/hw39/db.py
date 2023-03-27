from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.ext.asyncio import async_sessionmaker
from hw39 import settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine(settings.PGSQL_DATABASE_URL,echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()


async def db_init(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    app['db_session'] = async_session
    yield
        
