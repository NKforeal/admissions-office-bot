from aiogram import types, Bot


async def set_default_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command='start', description='🎫Получить талон'),
    ])
