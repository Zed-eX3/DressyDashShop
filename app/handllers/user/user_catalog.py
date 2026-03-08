from app.DataBase.models import async_session
from sqlalchemy import select
from app.DataBase.models import User
from app.DataBase.data.config import AdminR, AdminV

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.handllers.user.start import user_router


@user_router.callback_query(F.data == "catalog")
async def catalog_callback(callback: CallbackQuery):
    await callback.message.edit_text("Выьерите категорию товара!", reply_markup=get_catalog())


