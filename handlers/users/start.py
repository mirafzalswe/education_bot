from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.keys import menu


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f"<b>Qaytganingiz bilan {msg.from_user.full_name}!</b>\n O'zingiz istagan xizmatdan foydalanishingiz mumkin:", reply_markup=menu)

