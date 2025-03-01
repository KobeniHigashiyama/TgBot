from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создаём пустую клавиатуру с inline_keyboard=[]
admin_panel_keyboards_back_main_menu = InlineKeyboardMarkup(inline_keyboard=[])

# Создаём кнопку
admin_panel_button_main_menu = InlineKeyboardButton(text='Back to menu', callback_data='main_menu')

# Добавляем кнопку в клавиатуру через append
admin_panel_keyboards_back_main_menu.inline_keyboard.append([admin_panel_button_main_menu])
