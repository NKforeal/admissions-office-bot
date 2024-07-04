from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='➡️Продолжить', callback_data='continue')
    ],
    [
        InlineKeyboardButton(text='Контакты', callback_data='contacts')
    ],
])

