#bot
from bot.data.db import Database
from create_bot import bot, dp 
from bot.misc.filer import fich 
from bot.data.config import name_bot, path, url_channel_main, url_support_main
from bot.keyboards.user.user_key import back_in_start 

#module 
from aiogram import types
import base64
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

db = Database(path)

@dp.callback_query_handler(text='info_user')
async def call_profile_user(call: types.CallbackQuery):

    user_id = call.from_user.id 
    message_id = call.message.message_id
    first_name = call.from_user.first_name

    await bot.answer_callback_query(call.id, f"💼")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=fich(f"""
                                    <b>[📚] Информация {name_bot}
                                    
                                    [•] <a href='{url_channel_main}'>Игровой канал</a>
                                    [•] <a href='{url_support_main}'>Тех. поддержка</a></b>"""),
                                    reply_markup=back_in_start())