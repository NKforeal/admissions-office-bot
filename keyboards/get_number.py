from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_number_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Поделиться контактом', request_contact=True)]],
                                        resize_keyboard=True)
