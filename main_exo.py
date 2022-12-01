import asyncio

from aiogram import Bot,Dispatcher,executor
from confiq_exo import Bot_token

loop = asyncio.get_event_loop()
bot = Bot(Bot_token,parse_mode="HTML")
dp = Dispatcher(bot,loop=loop)

if __name__ =="__main__"
    from handlers import dp 


