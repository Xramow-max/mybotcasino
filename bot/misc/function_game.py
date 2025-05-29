# bot
from create_bot import bot, dp 
from bot.data.config import main_id
from bot.misc.filer import fich 
from bot.data.config import main_id

import bot.keyboards.channel_key.start_key_channel as chan

#module 
import asyncio 
import random

""" Функции для игр в канале """
""""""""""""""""""""""""""""""""


async def get_user_id(entata):

    """ Проверяем можем ли мы достать user_id"""

    try:
        user_id_entata = entata[0].user.id # Получаем user_id пользователя 
        return True
    except:
        await bot.send_message(main_id, fich(f"""
        <b>[❌] Произошла ошибка</b>
                                             
        <blockquote>⚠️ Включите пересылку сообщения в настройках!
        🎖 Это поможет вам в решении проблемы</blockquote>
        """),
        reply_markup=chan.channel_keyboard_stavka())
        return False
    

async def check_abuz_name(name, message):
    
    if 'отправил(а)' in name:
        await bot.delete_message(main_id, message.message_id)
        await bot.send_message(main_id, fich(f"""
        <b>😔 Мы заметили попытку абуза проекта!
                                             
        ❗️ Обратитесь к администратору, если считаете, что произошла ошибка!</b>
        """),
        reply_markup=chan.channel_keyboard_stavka())
        return False
    
    else:
        return True 
    

def get_stavka_soo(comment):
    try:
        comment_data = comment[1]
    except:
        comment_data = comment[0]

    st = comment_data.replace('💬', '')
    stavka = st.lower()
    return stavka

# Получаем сумму ставки
async def get_amount(match):
    
    value_str = match.group(1).replace(',', "").strip()  # Берем первую группу (сумма в скобках)
    try:
        value_ = float(value_str)  # Преобразуем строку в число с плавающей запятой
        value = round(value_, 2)   # Округляем до двух знаков
        return value
    except ValueError:
        print("Не удалось преобразовать строку в число.")
        return None


async def start_main_id_user(name, amount, stavka):

    soo = await bot.send_message(main_id, fich(f"""
    <b>🤵‍♂️ Ставка принята</b>
                                         
    <blockquote>👤 Игрок: <b>{name}</b>
    💰 Сумма: <b>{amount}$</b>
    🚀 Исход: <b>{stavka}</b></blockquote>
    """),
    reply_markup=chan.channel_keyboard_stavka())
    return soo 


async def handle_invalid_bet(stavka, value, soo):

    """ Проверяем правильно ли ввел ставку юзер"""

    if stavka not in ['п1', 'п2', 'м1', 'м2',
                      'победа1', 'победа2', 'меньше1', 'меньше2',
                      'чет', 'нечет',
                      'чёт', 'нечёт',
                      'сектор1', 'сектор2', 'сектор3',
                      'сектор 1', 'сектор 2', 'сектор 3',
                      'пл', 'плинко', 'plinko',
                      'баскет гол', 'баскет попал', 'гол', 'попал',
                        'баскет промах', 'баскет мимо',
                        'боул дуэль', 'боулинг дуэль',
                  'Боул дуэль', 'Боулинг дуэль']:
        
        values = value - (value * 0.1)
        await bot.delete_message(main_id, soo.message_id)
        await bot.send_message(main_id, fich(f"""
        <b>❌ Бот не распознал ставку!
                                             
        ⚠️ Обратитесь к администратору для возврата ставки
        Вы получите: {values}$</b>                                             
        """),
        reply_markup=chan.channel_keyboard_stavka())
        return False
    
    else:
        return True 
    


lock = asyncio.Lock()

from bot.handlers.channel_game.kybik.start_kybik_game import start_game_kybik
from bot.handlers.channel_game.plinko.start_plinko_game import start_game_plinko
from bot.handlers.channel_game.basket.start_basket_game import start_game_basket
from bot.handlers.channel_game.boul.start_boul_game import start_game_boul

async def await_check_stavka_game(value, soo, user_id, stavka):

    async with lock:
        if stavka in ['п1', 'п2',
                      'победа1', 'победа2',
                      'чет', 'нечет',
                      'чёт', 'нечёт',
                      'сектор1', 'сектор2', 'сектор3',
                      'сектор 1', 'сектор 2', 'сектор 3']:
            await start_game_kybik(stavka, value, user_id, soo)
        elif stavka in ['пл', 'плинко', 'plinko']:
            await start_game_plinko(stavka, value, user_id, soo)
        elif stavka in ['баскет гол', 'баскет попал', 'гол', 'попал',
                        'баскет промах', 'баскет мимо']:
            await start_game_basket(stavka, value, user_id, soo)
        elif stavka in ['боул дуэль', 'боулинг дуэль',
                  'Боул дуэль', 'Боулинг дуэль']:
            await start_game_boul(stavka, value, user_id, soo)
            
