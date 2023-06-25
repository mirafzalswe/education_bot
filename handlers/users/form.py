from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command

from aiogram import types
from loader import dp
from keyboards.default.exit import cancel_kb
from states.register import Profilestates
from keyboards.default.menu import menu_kb


@dp.message_handler(commands=['chiqish'], state='*')
async def cmd_cansel(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.reply("Royxadan otish toxtatildi")


@dp.message_handler(Text(equals="ro'yxatdan o'tish"))
async def cmd_regist(message: types.Message) -> None:
    await message.reply("Ro'yxadan otishni boshladik 😊 \n"
                         "ism va Familiyangizni tolliq kiriting !",
                        reply_markup=cancel_kb)
    await Profilestates.name.set()


@dp.message_handler(state=Profilestates.name)
async def load_name(message:types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply("yoshingizni kiriting !")
    await Profilestates.next()

@dp.message_handler(lambda messsage: not messsage.text.isdigit() or float(messsage.text) > 50, state=Profilestates.age)
async def check_age(message: types.Message):
    await message.reply("Yosh no'tog'ri kirtiglgan ❌!")


@dp.message_handler(state=Profilestates.age)
async def load_age(message:types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['age'] = message.text


    await message.reply("Telefon raqamingizni kirting !")
    await Profilestates.next()

@dp.message_handler(lambda messsage: not messsage.text.isdigit() or float(messsage.text) < 7, state=Profilestates.contakt)
async def check_phone(message:types.Message):
    await message.reply("Raqam notog'ri kiritlgan ❌ ")

@dp.message_handler(state=Profilestates.contakt)
async def load_cont(message:types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['contakt'] = message.text
    await message.reply("Royxadan otdingiz!",
                        reply_markup=menu_kb)

    await state.finish()
