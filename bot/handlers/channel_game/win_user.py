#bot
from create_bot import bot, dp
from bot.data.config import channel_info, client, main_id
from bot.misc.filer import fich 

import bot.keyboards.channel_key.start_key_channel as chan

# module
from aiogram import types
import asyncio
import random


async def payout_winnings(value_win, soo, user_id):

    """ Функция при победе пользователя"""

    await asyncio.sleep(1.3)
    try:
        rand = random.randint(1, 10000000000) # Рандомный номер счета
        await client.transfer(spend_id=rand, user_id=user_id, asset='USDT', amount=value_win)
        with open('bot/photo/win.jpg', 'rb') as video:
            await bot.send_photo(chat_id=main_id, 
                                photo=video,
                                caption=fich(f"""
                                <blockquote><b>👑 Победа..</b>
                                             
                                <b>💎 Сумма выигрыша: {value_win}$
                                💵 Ваш выигрыш зачислен на ваш CryptoBot кошелек</b></blockquote>
                                
                                                <<a href='https://t.me/+fw6LpzwAurhjM2M6'><b>PanWinNews</b></a> | a href='https://t.me/WaltrWh1te'><b>Support</b></a> | <a href='http://t.me/pantheonvin_Bot'><b>PanWinBot</b></a> 
                                                     \n <a href='https://t.me/+oA8tJCWhm-4wNmYy'><b>Adapter</b></a> | <a href='https://t.me/+Qypann3BaMtlOWUy'><b>Chat</b></a>"""),
                                reply_markup=chan.channel_keyboard_stavka(),
                                reply_to_message_id=soo.message_id)
            await asyncio.sleep(3)
    except Exception as e:
        print(e)
        with open('bot/photo/win.jpg', 'rb') as video:
            await bot.send_photo(chat_id=main_id, 
                                    photo=video,
                                    caption=fich(f"""
                                <blockquote><b>👑 Победа..</b>
                                             
                                <b>💎 Сумма выигрыша: {value_win}$
                                💵 Ваш выигрыш будет зачислен вручную!</b></blockquote>
                                
                                <<a href='https://t.me/+fw6LpzwAurhjM2M6'><b>PanWinNews</b></a> | a href='https://t.me/WaltrWh1te'><b>Support</b></a> | <a href='http://t.me/pantheonvin_Bot'><b>PanWinBot</b></a> 
                                                     \n <a href='https://t.me/+oA8tJCWhm-4wNmYy'><b>Adapter</b></a> | <a href='https://t.me/+Qypann3BaMtlOWUy'><b>Chat</b></a>"""),
                                    reply_markup=chan.channel_keyboard_stavka(),
                                    reply_to_message_id=soo.message_id)
            

            user_link = f'<a href="tg://user?id={user_id}"><b>Аккаунт</b></a>'
            await bot.send_message(
                            chat_id=channel_info,
                            text=fich(f"""  
                            <b>💸 Новая выплата в казино!</b>
                                      
                            <b>💰 Сумма: {value_win}$
                            👤 {user_link}</b>"""))
                            
            await asyncio.sleep(3)