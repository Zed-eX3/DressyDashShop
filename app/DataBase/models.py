from sqlalchemy import BigInteger, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    Id: Mapped[int] = mapped_column(
        primary_key=True
        ) 
    name: Mapped[str] = mapped_column(
        String(20)
        )
    tg_id = mapped_column(
        BigInteger, 
        unique=True
        )
    
    
class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(
        primary_key=True
        )
    name: Mapped[str] = mapped_column(
        String(20)
        )
    brand: Mapped[str] = mapped_column(
        String(20)
        )
    
    
class Item(Base):
    __tablename__ = 'Items'
        
    id: Mapped[int] = mapped_column(
        primary_key=True
        )
    name: Mapped[str] = mapped_column(
        String(25)
        )
    price: Mapped[int]
    description: Mapped[str] = mapped_column(
        String(100)
        )
    item_id: Mapped[str] = mapped_column(
        unique=True
        )
    photo_url: Mapped[str]
    amount: Mapped[int] 
    size: Mapped[str] = mapped_column(
        String(10)
        )
    
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    