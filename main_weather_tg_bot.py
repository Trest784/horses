import requests
from confiq_meteo import token_bot, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import message

bot = Bot(token=token_bot)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне город и я пришлю погоду")

@dp.message_handler(commands=["start"])
async def get_weather(message:types.Message):


    if __name__ == '__main__':
        executor.start_polling(dp)




    try:
        r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()


        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        await message.reply(
              f"Погода в городе:{city}\nТемпература:{cur_weather}C\n"
              f"Влажность:{humidity}\nДавление:{pressure} мм.рт.ст\nВетер:{wind}\n"
              f"хорошего дня!"
              )

    except:
        await message.reply("проверьте название города")