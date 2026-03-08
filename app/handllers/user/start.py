from app.DataBase.models import async_session
from sqlalchemy import select
from app.DataBase.models import User
from app.DataBase.data.config import AdminR, AdminV

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from app.keyboards.inline import get_catalog, get_menu
from app.handllers.admin.admin_menu import get_admin_menu
from app.keyboards.inline import comeback_to_menu

start_router = Router()

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
    
    



@start_router.message(CommandStart())
async def start_command(message: Message):
    tg_id = message.from_user.id
    full_name = message.from_user.full_name
    
    if str(AdminR) == str(tg_id):
        await message.answer('Здравствуй админ!', reply_markup=get_admin_menu())
        
    else:
        await message.answer("Привет! Это магазин кросовок!\nЕсли хочешь ознакомиться с товарами перейди в каталог!", reply_markup=get_menu())
        
        user = await get_user(tg_id)
        if user is None:
            # Сохраняем нового пользователя
            await add_user(tg_id, full_name)
        # else:
        #     await message.answer(f"С возвращением, {user.name}!")


@start_router.callback_query(F.data == "catalog")
async def catalog_callback(callback: CallbackQuery):
    await callback.message.edit_text("Выьерите категорию товара!", reply_markup=get_catalog())
    
    
@start_router.callback_query(F.data == "catalog")
async def catalog_callback(callback: CallbackQuery, message: Message):
    tg_id = message.from_user.id
    full_name = message.from_user.full_name
    await callback.message.edit_text(f"{full_name}\n{tg_id}", reply_markup=comeback_to_menu())
    

@start_router.callback_query(F.data == "start")
async def start_callback(callback: CallbackQuery, message: Message):
    tg_id = message.from_user.id
    full_name = message.from_user.full_name
    if str(AdminR) == str(tg_id):
            await callback.message.edit_text('Здравствуй админ!', reply_markup=get_admin_menu())
            
    else:
        await callback.message.edit_text("Привет! Это магазин кросовок!\nЕсли хочешь ознакомиться с товарами перейди в каталог!", reply_markup=get_menu())
            
        user = await get_user(tg_id)
        if user is None:
            # Сохраняем нового пользователя
            await add_user(tg_id, full_name)