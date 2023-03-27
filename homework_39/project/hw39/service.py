import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from hw39.models import Comment
from sqlalchemy.future import select

async def create_comment(app, text):
    db_rate = Comment(text = text, date_posted = datetime.datetime.now())
    print(app['db_session'])
    async with app['db_session']() as db:
        db.add(db_rate)
        await db.commit()
        await db.refresh(db_rate)
        return db_rate

async def get_comment(app):
    async with app['db_session']() as db:
        return await db.execute(select(Comment).order_by('date_posted'))