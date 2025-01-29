from aiogram import types
from aiogram.dispatcher import dispatcher
from aiogram.filters import Command
from keyboards.common_keyboards import get_start_keyboard

def register_common_handlers(dp: dispatcher):
    dp.message.register(start_command, Command(commands=['start']))
    dp.message.register(help_command, Command(commands=['help']))

async def start_command(message: types.Message):
    keyboard = get_start_keyboard()
    await message.answer("Стартуем!", reply_markup=keyboard)

async def help_command(message: types.Message):
    await message.answer("Это помощь!")