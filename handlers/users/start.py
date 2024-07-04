from datetime import datetime

import sqlalchemy.exc
from aiogram import Router, types, html
from aiogram.filters import Command

from DAO.users_dao import UsersDAO
from keyboards.main_menu import main_menu
from sqlalchemy.exc import IntegrityError
router = Router()


@router.message(Command(commands=['start']))
async def start_command(message: types.Message):
    username = message.from_user.username if message.from_user.username else ' '
    tg_id = message.from_user.id
    name = message.from_user.first_name if message.from_user.first_name else None
    last_name = message.from_user.last_name if message.from_user.last_name else None
    creation_date = datetime.utcnow()

    try:
        await UsersDAO.add(username=username,
                           tg_id=tg_id,
                           name=name,
                           last_name=last_name,
                           creation_date=creation_date
                           )

    except IntegrityError:
        await UsersDAO.update_by_tg_id(username=username,
                                       tg_id=tg_id,
                                       name=name,
                                       last_name=last_name,
                                       )

    await message.answer(html.bold(f'👋Здравствуйте {message.from_user.first_name}!\n\n'
                                   f'С помощью этого бота вы можете занять очередь в нашу приемную комиссию КАИТ №20.'),
                         reply_markup=main_menu)
