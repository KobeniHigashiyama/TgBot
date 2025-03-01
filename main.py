import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config.bot_config import dp, bot
from handler.admin_panel.create_post import router as create_post_router
from handler.admin_panel.deleate_post import router as delete_post_router
from handler.admin_panel.main_menu import router as main_menu_router
from handler.start.start import router as start_router

# Регистрируем роутеры
dp.include_router(create_post_router)
dp.include_router(delete_post_router)
dp.include_router(main_menu_router)
dp.include_router(start_router)

# Асинхронная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
