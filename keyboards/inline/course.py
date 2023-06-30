from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

days = InlineKeyboardMarkup(
    row_width = 2,
    inline_keyboard=[
        [
            InlineKeyboardButton('Toq kunlari', callback_data='Toq'),
            InlineKeyboardButton('Juft kunlari', callback_data='Juft'),
        ]
    ]
)


times = InlineKeyboardMarkup(
    row_width = 2,
    inline_keyboard=[
        [
            InlineKeyboardButton('Ertalab', callback_data='Ertalab'),
            InlineKeyboardButton('Kechki', callback_data='Kechki'),
        ]
    ]
)