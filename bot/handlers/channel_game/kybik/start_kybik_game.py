#bot
from create_bot import bot, dp 
from bot.data.config import main_id
import bot.keyboards.channel_key.start_key_channel as chan

from bot.handlers.channel_game.win_user import payout_winnings
from bot.handlers.channel_game.lose_user import payout_lose
#module
from aiogram import types 
import asyncio 



def get_game_coefficient(stavka):
    """
    Возвращает коэффициент для указанной ставки.
    """
    if stavka in ['чёт', 'чет' , 'нечёт', 'нечет', 'победа1', 'п1'
                  'победа2', 'п2', 'сектор1', 'сектор2', 'сектор3',
                      'сектор 1', 'сектор 2', 'сектор 3']:
        return 1.9
    else:
        # Если ставка не распознана
        return 1.9  # По умолчанию можно вернуть 1, если ставка не найдена
    


async def start_game_kybik(stavka, value, user_id_channel, soo):
    """ Игровая функция для ставок: Кубиком """

    two_dice_stavki = {
        'победа1': lambda d1, d2: d1 > d2,
        'п1': lambda d1, d2: d1 > d2,
        'победа2': lambda d1, d2: d1 < d2,
        'п2': lambda d1, d2: d1 > d2,
    }
    
    single_dice_stavki = {
        'чёт': [2, 4, 6],
        'чет': [2, 4, 6],
        'нечёт': [1, 3, 5],
        'нечет': [1, 3, 5],
        'сектор1': [1,2],
        'сектор2': [3,4],
        'сектор3': [5,6],
        'сектор 1': [1,2],
        'сектор 2': [3,4],
        'сектор 3': [5,6]
    }


    if stavka in single_dice_stavki:
        dice1 = await bot.send_dice(chat_id=main_id, reply_to_message_id=soo.message_id)
        value_dice = dice1.dice.value
        
        if value_dice in single_dice_stavki[stavka]:

            await asyncio.sleep(3.7)  # Время ожидания

            koef = get_game_coefficient(stavka)
            value_ = float(value) * koef
            value_win = round(value_, 2) # Считаем выигрыш пользователя
            
            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)
        else:
            await asyncio.sleep(3.7)  # Время ожидания
            
            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)

    elif stavka in two_dice_stavki:
        dice1 = await bot.send_dice(chat_id=main_id, reply_to_message_id=soo.message_id)
        value_dice1 = dice1.dice.value

        await asyncio.sleep(1.2)

        dice2 = await bot.send_dice(chat_id=main_id, reply_to_message_id=soo.message_id)
        value_dice2 = dice2.dice.value

        if two_dice_stavki[stavka](value_dice1, value_dice2):
            await asyncio.sleep(3.7)

            koef = get_game_coefficient(stavka)
            value_ = float(value) * koef
            value_win = round(value_, 2) # Считаем выигрыш пользователя
            
            """ Пользователь выиграл """
            await payout_winnings(value_win, soo, user_id_channel)
        else:
            await asyncio.sleep(3.7)

            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)