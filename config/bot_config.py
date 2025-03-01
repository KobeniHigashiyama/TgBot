from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
import logging
from aiogram.fsm.storage.memory import MemoryStorage


config = dotenv_values('./config/.env')
API_TOKEN = config['API_TOKEN']
ADMIN_ID = config['ADMIN_ID']


logging.basicConfig(level=logging.INFO)
bot = Bot(API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

