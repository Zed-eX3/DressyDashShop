from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from app.DataBase.data.config import AdminR, AdminV

class IsUser(BaseFilter):
    async def __call__(self, obj: Message | CallbackQuery) -> bool:
        user_id = obj.from_user.id
        return not (user_id in AdminR)