from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from aiogram import types
from loader import dp
from states.interactions import Register
from keyboards.default.keys import menu, phone


@dp.message_handler(CommandStart())
async def start_stage(msg: types.Message):
    await msg.answer(f"<b>Assalomu alaykum</b>, iltimos familyangiz va ismingizni kiriting! \n<i>Misol uchun: Falonchiyev(a) Falonchi</i>", reply_markup=ReplyKeyboardRemove(True))
    await Register.name.set()


@dp.message_handler(state=Register.name)
async def name_stage(msg: types.Message, state: FSMContext):
    await state.set_data(
        {
            'name': msg.text,
        }
    )
    await msg.reply(f"<b>Ajoyib {msg.text.split()[-1]}!</b>\nEndi pastdagi tugma yordamida telefon raqamingizni yuboring!", reply_markup=phone)
    await Register.next()


@dp.message_handler(state=Register.contact, content_types=types.ContentType.CONTACT)
async def contact_stage(msg: types.Message, state: FSMContext):
    await state.update_data(
        {
            'phone': str(msg.contact.phone_number),
        }
    )
    print(await state.get_data())
    # Reset all data from state
    await state.reset_data()
    # Finish state
    await state.finish()
    await msg.answer("O'zingiz istagan xizmatdan foydalanishingiz mumkin:", reply_markup=menu)
