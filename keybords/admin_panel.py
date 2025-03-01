from aiogram import types

# Создаём пустую клавиатуру с inline_keyboard=[]
admin_panel_keyboards_main_menu = types.InlineKeyboardMarkup(inline_keyboard=[])

# Создаём кнопки
admin_panel_button_create_post = types.InlineKeyboardButton(text='Создать пост', callback_data='create_post')
admin_panel_button_delete_post = types.InlineKeyboardButton(text='Удалить пост', callback_data='delete_post')

# Добавляем кнопки в один ряд с помощью .append()
admin_panel_keyboards_main_menu.inline_keyboard.append([
    admin_panel_button_create_post,
    admin_panel_button_delete_post
])
