from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from app.DataBase.data.config import AdminR, AdminV, Admins

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message | CallbackQuery) -> bool:
        user_id = message.from_user.id
        return user_id in Admins