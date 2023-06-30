from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.keys import menu, finish
from keyboards.inline.course import days
from states.interactions import CourseRegister, Support

@dp.message_handler(text='Ortga qaytish')
async def back_to_menu(msg: types.Message):
    await msg.answer("O'zingiz istagan xizmatdan foydalanishingiz mumkin:", reply_markup=menu)


@dp.message_handler(text="Kursga yo'zilish 📝")
async def course_register(msg: types.Message):
    await msg.answer_chat_action(action="Typing")
    await msg.answer("Sizni ro'yxatdan o'tkazishimiz uchun iltimos, so'ralgan barcham ma'lumotlarni to'g'ri kiriting! \nO'zingizga qulay vaqtni tanlang:", reply_markup=days)
    await CourseRegister.days.set()


@dp.message_handler(text='Support teacher 🧑‍🏫')
async def get_support(msg: types.Message):
    await msg.answer("O'zingizdagi muammoni batafsil yozib jo'natishingiz mumkin, ustozlarimizdan biri sizga javob qaytarishadi.\n" \
                     "Savollaringizga javob olib bo'lganingizdan so'ng Finish tugmasini bosing, aks xolda siz bilan aloqa uziladi!", reply_markup=finish)
    await Support.teacher.set()


@dp.message_handler(text="Administratsiya bilan bog'lanish 🙋‍♂️")
async def admin(msg: types.Message):
    await msg.answer('...')


@dp.message_handler(text="Finish ✅", state=Support.teacher)
async def admin(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer("O'zingiz istagan xizmatdan foydalanishingiz mumkin:", reply_markup=menu)