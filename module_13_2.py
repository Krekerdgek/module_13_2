#Задача "Бот поддержки (Начало)"
# ставим python 3.9
# ставим aiogram 2.25.1
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor

api = '8089404457:AAFRCwb80AfVsJbrh1QI-pp9Rwf2o_9Yqq8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)