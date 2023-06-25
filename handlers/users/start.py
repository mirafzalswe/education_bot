from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.regist import regist_bt
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleikum, <b>{message.from_user.full_name}!</b>\n"
                         f"ushbu botdan foydalanish uchun \n"
                         f"siz ro'yxadan otishingiz lozim",
                         reply_markup=regist_bt)


