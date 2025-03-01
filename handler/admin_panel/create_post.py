from aiogram import types, F, Router
from config.bot_config import bot
from keybords.admin_back import admin_panel_keyboards_back_main_menu

router = Router()  # Создаём роутер

@router.callback_query(F.data == 'create_menu')
async def admin_panel_create_post_callback(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.message.from_user.id,
                             message_id=callback_query.message.message_id)  # message_id вместо id
    await bot.send_message(callback_query.message.from_user.id,
                           'Create post', reply_markup=admin_panel_keyboards_back_main_menu)
