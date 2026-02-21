from app.DataBase.models import async_session
from sqlalchemy import select
from app.DataBase.models import User

async def add_user(tg_id: int, name: str):
    if len(name) > 20:
        name = name[:20]
    async with async_session() as session:
        user = User(tg_id=tg_id, name=name)
        session.add(user)
        await session.commit()
        
        
async def get_user(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        return result.scalar_one_or_none()