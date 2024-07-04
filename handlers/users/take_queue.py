from aiogram import types, Router, F, html
from aiogram.types import CallbackQuery

from DAO.users_dao import UsersDAO
from keyboards.take_queue_ikb import take_queue_ikb

router = Router()


async def take_queue(message: types.Message):
    await message.answer(html.bold('Нажмите Получить талон, чтобы занять очередь.'),
                         reply_markup=take_queue_ikb)


async def take_queue_cb(callback: CallbackQuery):
    await callback.message.answer(html.bold('Нажмите Получить талон, чтобы занять очередь.'),
                                  reply_markup=take_queue_ikb)


@router.callback_query(F.data == "get_queue_number")
async def show_queue_number(callback: CallbackQuery):
    user = await UsersDAO.find_one_or_none(tg_id=callback.from_user.id)
    last_number = 0
    if not user.queue_number:
        users = await UsersDAO.find_all_scalars()

        for user in users:
            if user.queue_number >= last_number:
                last_number = user.queue_number

        last_number += 1

        await UsersDAO.update_by_tg_id(tg_id=callback.from_user.id, queue_number=last_number)

    await callback.message.answer(
        html.bold(f"Ваш талон - №{user.queue_number if user.queue_number else last_number}\n\n"
                  f"Покажите это сообщение сотруднику колледжа."))
