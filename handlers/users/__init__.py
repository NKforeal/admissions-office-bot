from aiogram import Dispatcher, Router
from .start import router as start_router
from .contacts_handler import router as contacts_handler_router
from .get_number import router as get_number_router
from .take_queue import router as take_queue_router

def init_user_router(dp: Dispatcher):
    router = Router()
    router.include_router(start_router)
    router.include_router(contacts_handler_router)
    router.include_router(get_number_router)
    router.include_router(take_queue_router)
    dp.include_router(router)
