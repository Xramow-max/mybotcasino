#bot
from create_bot import bot, dp 
from bot.data.config import main_id
from bot.misc.filer import fich 

import bot.keyboards.channel_key.start_key_channel as chan

#module 
from aiogram import types
import asyncio 

async def payout_tie_boul(value, soo, user_id_channel):

    """ Функция при Проигрыше пользователя"""

    await asyncio.sleep(1.3)
    with open('bot/photo/tie.jpg', 'rb') as video:
            await bot.send_photo(chat_id= main_id,
                                        photo=video,
                                        caption=fich(f"""
                                                <blockquote><b>🤝 Ничья..</b>
                                                     
                                                <i>Не переставай верить в удачу и она повернется к тебе лицом!</i></blockquote>
                                                     
                                                <b>⭐️ Повезет в следующий раз!</b>
                                                     
                                                <<a href='https://t.me/+fw6LpzwAurhjM2M6'><b>PanWinNews</b></a> | a href='https://t.me/WaltrWh1te'><b>Support</b></a> | <a href='http://t.me/pantheonvin_Bot'><b>PanWinBot</b></a> 
                                                     \n <a href='https://t.me/+oA8tJCWhm-4wNmYy'><b>Adapter</b></a> | <a href='https://t.me/+Qypann3BaMtlOWUy'><b>Chat</b></a> """),
                                        reply_markup=chan.channel_keyboard_stavka(),
                                        reply_to_message_id=soo.message_id)
            await asyncio.sleep(3)