from aiogram import types, F, Router
from config.bot_config import bot
from keybords.admin_panel import admin_panel_keyboards_main_menu

router = Router()  # Создаём роутер

@router.callback_query(F.data == 'main_menu')
async def admin_main_menu_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.message.from_user.id,
                             message_id=callback_query.message.message_id)  # message_id вместо id
    await bot.send_message(callback_query.message.from_user.id,
                           'in main menu', reply_markup=admin_panel_keyboards_main_menu)
