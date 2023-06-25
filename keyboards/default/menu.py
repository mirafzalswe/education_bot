from aiogram.types.reply_keyboard import KeyboardButton,ReplyKeyboardMarkup



menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kursga yo'zilish 📝"),
            KeyboardButton("Support teacher 🧑‍🏫"),
        ],
        [
            KeyboardButton("Administratsiya bilan bog'lanish 🙋‍♂️")
        ]
    ],
)
