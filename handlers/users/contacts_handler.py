from aiogram import Router, types, F, html
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

router = Router()

phone1 = html.code("+7(499)164-86-95")
phone2 = html.code("+7(499)164-49-30")
phone3 = html.code("+7(901)181-20-20")
email = html.code("priem@kait20.ru")


@router.callback_query(F.data == 'contacts')
async def show_contacts(callback: CallbackQuery):
    await callback.message.answer(html.bold('Наши контакты:\n\n'
                                            f'☎️\n'
                                            f'{html.code(phone1)}\n'
                                            f'{html.code(phone2)}\n'
                                            f'{html.code(phone3)}\n'
                                            f'---\n'
                                            f'✉️\n{html.code(email)}\n'
                                            f'---\n'),
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=
                                                                    [[InlineKeyboardButton(text='Наш сайт',
                                                                                           url='https://kait20.mskobr.ru/')],
                                                                     [InlineKeyboardButton(text='📍Адрес',
                                                                                           url='https://yandex.ru/maps/-/CDvz7RZK')],
                                                                     ]))
