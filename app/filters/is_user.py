from aiogram.types import Message
from aiogram.filters import BoundFilter
from app.DataBase.data.config import AdminR, AdminV


class Admin(BoundFilter):


    async def check(self, message: Message):
        return message.from_user.id not in AdminR or message.from_user.id not in AdminV