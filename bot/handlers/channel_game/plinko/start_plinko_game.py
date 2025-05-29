#bot
from create_bot import bot, dp
from bot.data.config import main_id, path
from bot.data.db import Database
from bot.handlers.channel_game.win_user import payout_winnings
from bot.handlers.channel_game.lose_user import payout_lose

#module
from aiogram import types
import asyncio

db = Database(path)

async def start_game_plinko(stavka, value, user_id_channel, soo):
    """ Игровая функция для ставок: Плинко """


    if stavka in ['пл', 'плинко', 'plinko']:
        await asyncio.sleep(1)
        dice = await bot.send_dice(main_id, reply_to_message_id=soo.message_id)

        if dice.dice.value in [1]:

            await asyncio.sleep(3.7)  # Время ожидания
            
            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)

        elif dice.dice.value in [2]:

            await asyncio.sleep(3.7)  # Время ожидания

            koef = 0.3 
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        elif dice.dice.value in [3]:

            await asyncio.sleep(3.7)  # Время ожидания
                    
            koef = 0.9 
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        elif dice.dice.value in [4]:

            await asyncio.sleep(3.7)  # Время ожидания

            koef = 1.1
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        elif dice.dice.value in [5]:
                    
            await asyncio.sleep(3.7)  # Время ожидания

            koef = 1.35
            value_ = float(value) * koef
            value_win = round(value_, 2)

            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)

        elif dice.dice.value in [6]:

            await asyncio.sleep(3.7)  # Время ожидания

            koef = 1.9
            value_ = float(value) * koef
            value_win = round(value_, 2)