#bot
from create_bot import bot, dp
from bot.data.config import main_id # Конфиги

from bot.handlers.channel_game.win_user import payout_winnings
from bot.handlers.channel_game.lose_user import payout_lose
from bot.handlers.channel_game.boul.boul_tie import payout_tie_boul

#module
from aiogram import types
import asyncio

def get_game_coefficient_boul(stavka, user_id_channel):
    """
    Возвращает коэффициент для указанной ставки.
    """
    if stavka in ['боул дуэль', 'боулинг дуэль',
                  'Боул дуэль', 'Боулинг дуэль']:
        return 1.8

    else:
        # Если ставка не распознана
        return 1.8  # По умолчанию можно вернуть 1, если ставка не найдена

async def start_game_boul(stavka, value, user_id_channel, soo):
    """ Игровая функция для ставок: Боулинг """


    dice = await bot.send_dice(main_id, emoji='🎳', reply_to_message_id=soo)
    value_dice = dice.dice.value

    await asyncio.sleep(1)  # Время ожидания

    dice_bot = await bot.send_dice(main_id, emoji='🎳', reply_to_message_id=soo)
    value_dice_bot = dice_bot.dice.value
        
    if value_dice > value_dice_bot:
        await asyncio.sleep(2.7)  # Время ожидания

        koef = get_game_coefficient_boul(stavka, user_id_channel)
        value_ = float(value) * koef
        value_win = round(value_, 2) # Считаем выигрыш пользователя
            
        """ Пользователь выиграл """
        await payout_winnings(value_win, soo, user_id_channel)
        
    elif value_dice < value_dice_bot:
            await asyncio.sleep(2.7)  # Время ожидания
            
            """ Пользователь проиграл """
            await payout_lose(soo, user_id_channel, value)

    else:

            await asyncio.sleep(2.7)  # Время ожидания
            
            """ Ничья """
            await payout_tie_boul(value, soo, user_id_channel)