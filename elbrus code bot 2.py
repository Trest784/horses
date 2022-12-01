import time
import logging

from aiogram import Bot, Dispatcher, executor, types

token = "5972491164:AAGsPbPSriewaq9XV3TrJP8eyMl55A-MwOk"
msg = "программировал ли ты сегодня"


bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start']) # декоратор который обратывает входные сообщения в форме сообщений
def start_handler(message: types.Message): #функция обработки сообщений
    user_id = message.from_user.id  # переменная оботбражающия юзер айди
    user_full_name = message.from_user.full_name # переменная полное имя пользователя
    logging.info(f'{"user_id"}{"user_full_name"},{time.asctime()}') #логнаирование состояний которое указывает и сохраняет определенные данные
    await message.reply("привет{"user_full_name"}") #способ формы ответа,авайт форма ретурна


    for i in range(10):
        time.sleep(2)

    await bot.send_message(user_id,msg.format(user_full_name))

if __name__ == '__main__': # почему это применимо здесь мне не понятно и почему он решил это применить я не понимаю
    executor.start.polling(dp) #функция соеденения с интернетом 


    #у меня тоже не работает не хуя данный бот в телеге полный пиздос поччему я не понимаю если я все в точности скопировал