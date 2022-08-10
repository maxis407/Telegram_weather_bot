import requests
from cfg import bot_token
import datetime
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(command = ["start"])
async def start_command(message: types.Message):
    await message.answer("Привет! Напиши название города для определения его погоды :)")


executor.start_polling(dp)
