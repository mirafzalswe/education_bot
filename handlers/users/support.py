from aiogram import types
from aiogram.dispatcher.filters import IsReplyFilter

from loader import dp, bot
from states.interactions import Support
from data.config import TEACHERS as teachers
from filters.customs import IsTeacher


@dp.message_handler(IsReplyFilter(True), IsTeacher())
async def reply_teacher(msg: types.Message):
    user_id = int(msg.reply_to_message.text.split()[-1])
    await msg.reply_to_message.bot.send_message(user_id, msg.text)


@dp.message_handler(state=Support.teacher)
async def connection(msg: types.Message):
    message = msg.text + f"\n\n<i>{msg.from_user.id}</i>"
    for teacher in teachers:
        await bot.send_message(teacher, message)
    



