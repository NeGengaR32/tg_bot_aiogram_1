from aiogram import types
from aiogram.dispatcher import dispatcher
from aiogram.filters import Command
import requests
from config import WEATHER_API_KEY

def register_weather_handlers(dp: dispatcher):
    dp.message.register(weather_command, Command(commands=['weather']))

async def weather_command(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Пожалуйста, укажите город. Например: /weather Москва")
        return
    
    city = args[1]  
    
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
        )
        data = response.json()
        
        if data ['cod'] != 200:
            await message.answer("Город не найден")
            return
        
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        
        await message.answer(f"Погода в {city}: {temperature}°C, {description}")
        
    except Exception as e:
        await message.answer("Что-то пошло не так с запроссом погоды!")
        print(e)