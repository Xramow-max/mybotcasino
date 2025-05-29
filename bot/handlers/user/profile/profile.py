#bot
from bot.data.db import Database
from create_bot import bot, dp 
from bot.misc.filer import fich 
from bot.data.config import name_bot, path
import bot.misc.function as functions
from bot.keyboards.user.profile_key.profile_key import start_profile_key

#module 
from aiogram import types
import base64
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

db = Database(path)

@dp.callback_query_handler(text='profile_user', state='*')
async def call_profile_user(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id 
    message_id = call.message.message_id
    first_name = call.from_user.first_name

    await bot.answer_callback_query(call.id, f"💼")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=fich(f"""
                                    <b>[👤] Профиль {name_bot}
                                    
                                    [🆔] ID: <code>{user_id}</code>
                                    [👀] Name: <code>{first_name}</code>
                                    [💵] Баланс: <code>{db.get_balance(user_id)}$</code>
                                    [💸] Сыграно на: <code>{db.get_turnover(user_id)}$</code>
                                    [💰] Кол-во ставок: <code>{db.get_games(user_id)} шт.</code></b>"""),
                                    reply_markup=start_profile_key())