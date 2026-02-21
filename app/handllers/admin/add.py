import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.DataBase.models import Item
from app.DataBase.models import async_session

add_router = Router


async def add_item(name: str, price: int, description: str, item_id: str, photo_url: str, available: bool, amount: int, size: str):
    if len(name) > 25:
        name = name[:25]
    if len(description) > 100:
        description = description[:100]
    
    async with async_session() as session:
        item = Item(name=name, price=price, description=description, item_id=item_id, photo_url=photo_url, available=available, amount=amount, size=size)
        session.add(item)
        await session.commit()

@add_router.callback_query(F.data == 'add')
async def add_item(callback: CallbackQuery, message: Message):
    await callback.message.edit_text("Напишите товар:")
    item = message.text
    await message.answer(f'название товара: {item}')
    
    