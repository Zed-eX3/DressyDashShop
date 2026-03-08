# from app.DataBase.models import async_session
# from sqlalchemy import select
# from app.DataBase.models import User
# from app.DataBase.data.config import AdminR, AdminV

# from aiogram import Router, F
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message, CallbackQuery

# profile_router = Router()

# @profile_router.callback_query(User, AdminR, F.data == "profile")
# async def profile_callback(callback: CallbackQuery, message: Message):
#     tg_id = message.from_user.id
#     full_name = message.from_user.full_name
#     await callback.message.edit_text(f"Профиль\n{full_name}\n{tg_id}")

