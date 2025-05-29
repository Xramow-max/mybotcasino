# main
from create_bot import bot, dp 

from bot.misc.filer import fich
from bot.data.db import Database
from bot.data.config import path, name_bot, username_bot, channel_info
from bot.keyboards.user.profile_key.profile_key import back_in_profile 

# other
import base64
from aiogram import types 

db = Database(path)

@dp.callback_query_handler(text='dell_balance')
async def call_out_ref(call: types.CallbackQuery):

    user_id = call.from_user.id 

    balance = db.get_balance(user_id)

    if balance > 0:
        await bot.answer_callback_query(call.id,f"✅ Ваш баланс поставлен на выплату! Обратитесь к владельцу", show_alert=True)
        db.minus_balance(balance, user_id)

        user_link = f'<a href="tg://user?id={user_id}"><b>Аккаунт</b></a>'
        await bot.send_message(
                            chat_id=channel_info,
                            text=fich(f"""  
                            <b>💸 Новая выплата в казино!
                            💵 Выплата из бота!</b>
                                      
                            <b>💰 Сумма: {balance}$
                            👤 {user_link}</b>"""))
    else:
        await bot.answer_callback_query(call.id,f"❌ Ваш баланс равен 0!", show_alert=True)