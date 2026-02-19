from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from app.keyboards.inline import get_catalog, get_menu
from app.function import add_user, get_user

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Привет! Это магазин кросовок!\nЕсли хочешь ознакомиться с товарами перейди в каталог!", reply_markup=get_menu())
    tg_id = message.from_user.id
    full_name = message.from_user.full_name
    
    user = await get_user(tg_id)
    if user is None:
        # Сохраняем нового пользователя
        await add_user(tg_id, full_name)
    # else:
    #     await message.answer(f"С возвращением, {user.name}!")

@router.callback_query(F.data == "catalog")
async def catalog_callback(callback: CallbackQuery):
    await callback.message.edit_text("Выьерите категорию товара!", reply_markup=get_catalog())