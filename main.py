import asyncio
from datetime import datetime

from aiogram import Dispatcher, Bot, Router, html
from aiogram.client.default import DefaultBotProperties

from DAO.users_dao import UsersDAO
from config import settings

from handlers.users import init_user_router
from utils.set_bot_commands import set_default_commands


router = Router()


@router.startup()
async def on_start_up_notify_callback(bot: Bot):
    await set_default_commands(bot)

    for admin in settings.ADMINS_ID:
        try:
            users = await UsersDAO.find_all_mapping()

            text = html.bold('Бот успешно запущен!\n\n'
                             f'Количество пользователей - {len(users)}')

            await bot.send_message(chat_id=admin, text=text)

        except Exception as err:
            print(err)


# SAVE LOGS
@router.startup()
async def clear_queue(bot: Bot):
    asyncio.create_task(scheduler(bot))


async def scheduler(bot: Bot):
    while True:
        await asyncio.sleep(1)

        if datetime.now().strftime("%H:%M:%S") == '23:59:59':
            await UsersDAO.update(queue_number=0)

            for admin in settings.ADMINS_ID:
                await bot.send_message(text=f"Сегодняшняя очередь успешно сброшена.", chat_id=admin)


async def main():
    dp = Dispatcher()

    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

    init_user_router(dp)

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main=main())
