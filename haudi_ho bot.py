# данный скрипт сделан на Pytelegam bot api

import telebot
token = '5570764592:AAH3eIZV26xW2tudIfB_FiXpal7n02wa4uY'

bot = telebot.Telebot(token) # это просто имя переменной что типо бот это токен взятый из под фатера

@bot.message_handler(commands=['start']) # заголовок отвечающий за текствовое сообщение приветствия 
def welcome(message):

@bot.message_handler(content_types = ['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)


