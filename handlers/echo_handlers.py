from aiogram import types
from aiogram.dispatcher import dispatcher

def register_echo_handlers(dp: dispatcher):
    dp.message.register(echo_message)

async def echo_message(message: types.Message):
    await message.answer(message.text)