#bot
from create_bot import bot, dp 
from bot.data.config import main_id, path
from bot.misc.filer import fich 
from bot.data.db import Database

import bot.keyboards.channel_key.start_key_channel as chan
from bot.misc.function import check_referal_payment 

#module 
from aiogram import types
import asyncio 

db = Database(path)

async def payout_lose(soo, user_id, amount):

        """ Функция при Проигрыше пользователя"""

        db.plus_games(user_id)

        await asyncio.sleep(1.3)
        with open('bot/photo/lose.jpg', 'rb') as video:
                await bot.send_photo(chat_id= main_id,
                                        photo=video,
                                        caption=fich(f"""
                                                <blockquote><b>📛 Неудача..</b>
                                                     
                                                <i>Не переставай верить в удачу и она повернется к тебе лицом!</i></blockquote>
                                                     
                                                <b>⭐️ Повезет в следующий раз!</b>
                                                     
                                                <<a href='https://t.me/+fw6LpzwAurhjM2M6'><b>PanWinNews</b></a> | a href='https://t.me/WaltrWh1te'><b>Support</b></a> | <a href='http://t.me/pantheonvin_Bot'><b>PanWinBot</b></a> 
                                                     \n <a href='https://t.me/+oA8tJCWhm-4wNmYy'><b>Adapter</b></a> | <a href='https://t.me/+Qypann3BaMtlOWUy'><b>Chat</b></a>"""),
                                        reply_markup=chan.channel_keyboard_stavka(),
                                        reply_to_message_id=soo.message_id)
                await check_referal_payment(user_id, amount)
                await asyncio.sleep(2)