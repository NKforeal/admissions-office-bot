from aiogram import types, Router, F, html
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from DAO.users_dao import UsersDAO

from fsm.get_phone_fsm import GetNumberFSM
from handlers.users.take_queue import take_queue, take_queue_cb

from keyboards.get_number import get_number_markup


router = Router()


@router.callback_query(F.data == 'continue')
async def get_number(callback: CallbackQuery, state: FSMContext):
    user = await UsersDAO.find_one_or_none(tg_id=callback.from_user.id)

    if user.phone_number:
        await take_queue_cb(callback)
        return

    await state.set_state(GetNumberFSM.get_phone)
    await callback.message.answer(html.bold('Чтобы занять очередь вы должны поделиться контактом:'),
                                  reply_markup=get_number_markup)


@router.message(GetNumberFSM.get_phone)
async def get_number_success(message: types.Message, state: FSMContext):
    await UsersDAO.update_by_tg_id(tg_id=message.from_user.id, phone_number=message.contact.phone_number)
    await message.answer(text=html.bold(f'Вы успешно поделились контактом {html.code(message.contact.phone_number)}'),
                         reply_markup=types.ReplyKeyboardRemove())

    await take_queue(message)
    await state.clear()

