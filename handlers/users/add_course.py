import statistics

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from states.add_course import AddCourseState
from aiogram import types
from loader import dp


@dp.message_handler(Text(equals="Kursga yo'zilish 📝"))
async def add_new(messsage:types.Message, state:FSMContext) -> None:
    await messsage.reply("qaysi kursga yozilmoxchi bolganizni yozing")
    await AddCourseState.text.set()


@dp.message_handler(state=AddCourseState.text)
async def load_pupils(message:types.Message, state:FSMContext) -> None:
    async with state.proxy() as data:
        data['text'] = message.text

    await message.reply("Kurga yozilganingiz uchun raxmat")
    await state.finish()


