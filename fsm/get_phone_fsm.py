from aiogram.fsm.state import StatesGroup, State


class GetNumberFSM(StatesGroup):
    get_phone = State()
