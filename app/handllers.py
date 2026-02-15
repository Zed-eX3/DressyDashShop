from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from app.keyboards.inline import get_catalog, get_menu


router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Это магазин кросовок!\nЕсли хочешь ознакомиться с товарами перейди в каталог!", reply_markup=get_menu())
    

@router.callback_query(F.data == "catalog")
async def catalog_callback(callback: CallbackQuery):
    await callback.message.edit_text("Выьерите категорию товара!", reply_markup=get_catalog())