from aiogram import types, Dispatcher, executor, Bot
from tran_con import token_bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

bot = Bot(token_bot)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
b1 = KeyboardButton(text="со стикером")
b2 = KeyboardButton(text="без стикера")
kb.add(b1).insert(b2)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(text="эхо бот со стиками и без", reply_markup=kb)


@dp.message_handler(Text(equals='без стикера')
async def with_stick(message: types.Message):
    await message.reply("ехо будет без стикера")


@dp.message_handler(Text(equals='Со стикером')
async def without_stick(message: types.Message):
    await message.reply("ведите слово и получите эхо со стикером")



#@dp.message_handler()
#async def echo(message: types.Message):
#   await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)