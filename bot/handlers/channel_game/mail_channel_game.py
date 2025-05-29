#bot
from create_bot import bot, dp 
from bot.data.db import Database
from bot.data.config import logs_id, path
import bot.misc.function_game as functions_game

# module 
from aiogram import types 
import re 

db = Database(path)

@dp.channel_post_handler()
async def post_message_channel(message: types.Message):

    if message.chat.id == logs_id: # Проверка на обработку бота в канале логов 
        entata = message.entities 
        if await functions_game.get_user_id(entata):
            user_id_channel = entata[0].user.id
            name = entata[0].user.first_name
            comment = message.text.split('💬 ')  # Получаем комментарий для поиска ставки

            if await functions_game.check_abuz_name(name, message): # Проверка на абуз через ник

                stavka = functions_game.get_stavka_soo(comment) # Берем ставу из комментария
                match = re.search(r'отправил\(а\).*?\(\$(.+?)\)', message.text) # Берем строку с суммой ставки
                value = await functions_game.get_amount(match) # Получаем сумму ставки в типе INT

                soo = await functions_game.start_main_id_user(name, value, stavka) # Обрабатываем ставку в канал
                if await functions_game.handle_invalid_bet(stavka, value, soo): # Проверяем, правильно ли ввел ставку юзер
                    db.plus_turnover(value, user_id_channel)
                    await functions_game.await_check_stavka_game(value, soo, user_id_channel, stavka) # Играем ставку в канале 