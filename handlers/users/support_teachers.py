from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command

from aiogram import types
from loader import dp

from states.support_teachers import TeachersState

@dp.message_handler(Text(equals=("Support teacher 🧑‍🏫")))
async def cmd_teachers(message: types.Message) -> None:
    await message.reply("<b>Support teacherga xabarni quydagicha jonating: </b>\n"
                        "Men (falonchi) mavzuga tushunmadim \n"
                        "Yoke Men (falonchi) mavzulardan qolip ketdim !")
    await TeachersState.text.set()

@dp.message_handler(state=TeachersState.text)
async def check_txt(message:types.Message, state:FSMContext) -> None:
    async with state.proxy() as data:
        data['text'] = message.text
    await message.reply("Xabaringiz jonatildi \n"
                        "tez orada siz bilan bog'lanamiz \n"
                        "iltimos kuting.....")
    await state.finish()




