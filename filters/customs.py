from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import TEACHERS

class IsAdmin(BoundFilter):
    async def check(self, msg: types.Message):
        user = await msg.chat.get_member(msg.from_user.id)
        return user.is_chat_admin()


class IsTeacher(BoundFilter):
    async def check(self, msg: types.Message):
        teacher = await msg.chat.get_member(msg.from_user.id)
        return str(teacher.user.id) in TEACHERS

