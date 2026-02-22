from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from app.DataBase.data.config import AdminR, AdminV

class IsAdmin(BaseFilter):
    async def __call__(self, obj: Message | CallbackQuery) -> bool:
        user_id = obj.from_user.id
        return user_id in AdminR or user_id in AdminV