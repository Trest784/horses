# этот код работает у чувака, у меня не хуя. я сейчас по строчно распишу
# что происходит что происходит и пойду к следующему видосу где чуть по лучше разясняют


from aiogram import Bot,types #это строчка мне не понятна она трактуется как перевод бота , что мне не понятно так я не понимаю что конкретно импортируется из аиограмма
from aiogram.dispatcher import dispatcher # здесь импортируется диспатчер, диспатчер это то что обрабатывает все объекты и апдейты то есть сообщение сколько время обрабатывает диспатчер
from aiogram.utils import executor # непонятно то же что это тип из видео говорит что именно экзекьютор связывает код, интернет и бот в телеге на сколько я понял
# но парень из комментариев пичет что,
# Аиограм умеет работать в двух режимах - polling и webhooks.
# Как я понял, executor позволяет остальным механизмам бота абстрагироваться от используемого режима.
# Например,
# start_polling() просто создаёт реактор (loop) asyncio и запускает в нём задачу self.dispatcher.start_polling(),
# а потом ждёт сигнала завершения. Ну и еще дергает обработчики on_startup и on_shutdown. Это можно сделать и вручную, при необходимости.
# webhooks использует aiohttp для реализации веб-сервера, который будет получать запросы от telegram.
#
#
#
#
#





import os     #  непонятно как работает



bot = Bot(token=os.getnv(''))     # токен запускает  и импортирует код токена из самого телеграмма
dp=Dispatcher(bot)   # глобальное имя диспетчера

@dp.message_handler()  # хандлер это функция принимающая все входящий в бот запросы
async def echo_send(message:types.Message): # функция вопросов и ответов
    await message.answer(message.text)  # вопрос
    await message.reply(message.text)   # ответ от бота в (то что он в форме текста, может быть и форме аудиоссобщения)
    await bot.send_message(message.from_user.id, message.text)
    # эвейт форма ответа   внутри хендлера - типо стока обозначающая некий модуль вопроса и ответа



executor.start_polling(dp, skip_updates=True)
#форма  связи с телеграмом и кодом 

# этот бот не работает на мой взгляд по причине что я не хуй не сделал окружения про которое он говорил в начале