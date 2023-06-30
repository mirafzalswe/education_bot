from aiogram import types
from aiogram.dispatcher import FSMContext
from asyncio import sleep

from loader import dp, bot 
from states.interactions import CourseRegister
from keyboards.inline.course import times
from keyboards.default.keys import menu
from data.config import ADMIN


@dp.callback_query_handler(state=CourseRegister.days)
async def get_day(msg: types.CallbackQuery, state: FSMContext):
    await msg.message.delete()
    await state.set_data({
        'days': msg.data
    })
    await CourseRegister.next()
    mes = await msg.message.answer("O'zingizga qulay vaqt oralig'ini kiriting:", reply_markup=times)



@dp.callback_query_handler(state=CourseRegister.times)
async def get_day(msg: types.CallbackQuery, state: FSMContext):
    await msg.message.delete()
    await state.update_data({
        'times': msg.data,
    })
    data = await state.get_data()
    text = f"Yangi o'quvchi ro'yxatdan o'tdi!\n\nKunlar: {data['days']} \nVaqt: {data['times']}"
    await bot.send_message(ADMIN, text)

    await state.finish()
    await msg.message.answer("Tabriklayman ro'yxatdan muvaffaqiyatli o'tdingiz, tez orada siz bilan bog'lanmiz!", reply_markup=menu)

