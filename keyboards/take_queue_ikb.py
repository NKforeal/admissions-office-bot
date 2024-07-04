from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

take_queue_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Получить талон', callback_data='get_queue_number')
    ],
])
