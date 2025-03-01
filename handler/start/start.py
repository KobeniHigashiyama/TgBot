from aiogram import types, Router
from aiogram.filters import Command  # Импортируем Command для фильтрации команд
from config.bot_config import bot, ADMIN_ID
from keybords.admin_panel import admin_panel_keyboards_main_menu

router = Router()  # Создаём роутер


@router.message(Command("start"))  # Используем Command вместо commands=['start']
async def start(message: types.Message):
    user_id = str(message.from_user.id)  # Приводим user_id к строке для корректного сравнения

    if user_id == ADMIN_ID:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Вы админ!',
            reply_markup=admin_panel_keyboards_main_menu
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Вы не админ!'
        )
