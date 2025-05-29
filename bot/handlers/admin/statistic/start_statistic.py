# main
from create_bot import bot, dp 
from bot.data.config import path, name_bot
from bot.misc.filer import fich
import bot.misc.function as functions
from bot.data.db import Database
from bot.keyboards.admin.start_admin_panel import back_in_panel_adm

# other
from aiogram import types 
import base64

db = Database(path)

@dp.callback_query_handler(text='statistic')
async def call_statistic(call: types.CallbackQuery):

    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"📊 Статистика")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=fich(f"""
                                    <b>📊 Статистика {name_bot}
                                    
                                    <blockquote>🎁 Кол-во юзеров: <code>{db.count_user()} чел.</code>
                                    💵 Оборот казино: <code>{db.count_turnover()}$</code>
                                    🎲 Всего ставкок: <code>{db.count_games()} шт.</code>
                                    ⚡️ В казне: <code>{await functions.get_balance_kazna()}$</code></blockquote></b>"""),
                                    reply_markup=back_in_panel_adm())