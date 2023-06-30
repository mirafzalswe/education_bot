from aiogram.types.reply_keyboard import KeyboardButton,ReplyKeyboardMarkup



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kursga yo'zilish 📝"),
            KeyboardButton("Support teacher 🧑‍🏫"),
        ],
        [
            KeyboardButton("Administratsiya bilan bog'lanish 🙋‍♂️")
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True
)


phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Raqam yuborish", request_contact=True),
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True
)


back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Ortga qaytish')
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True
)


finish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Finish ✅')
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True
)