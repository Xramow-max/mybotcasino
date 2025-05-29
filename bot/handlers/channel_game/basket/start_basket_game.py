#bot
from create_bot import bot, dp
from bot.data.config import main_id, path
import bot.misc.function as functions
from bot.data.db import Database

from bot.handlers.channel_game.win_user import payout_winnings
from bot.handlers.channel_game.lose_user import payout_lose

#module
from aiogram import types
import asyncio

db = Database(path)

async def start_game_basket(stavka, value, user_id_channel, soo):
    """ Игровая функция для ставок: Баскетбол """


    if stavka in ['баскет промах', 'баскет мимо']:
        await asyncio.sleep(1)
        dice = await bot.send_dice(main_id, emoji='🏀', reply_to_message_id=soo.message_id)

        if dice.dice.value not in [4, 5]:

            await asyncio.sleep(3.7)  # Время ожидания

            koef = 1.4 
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        else:
            
            await asyncio.sleep(3.7)  # Время ожидания
            
            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)
        
    elif stavka in ['баскет гол', 'баскет попал', 'гол', 'попал']:
        await asyncio.sleep(1)
        dice = await bot.send_dice(main_id, emoji='🏀', reply_to_message_id=soo.message_id)

        if dice.dice.value in [4, 5]:
            await asyncio.sleep(3.7)  # Время ожидания

            koef = 1.4 
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        else:
            
            await asyncio.sleep(3.7)  # Время ожидания
            
            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)