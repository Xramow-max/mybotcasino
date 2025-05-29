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

@dp.callback_query_handler(text='referal_program')
async def call_referal_program(call: types.CallbackQuery):

    user_id = call.from_user.id 
    message_id = call.message.message_id

    url_link = f'https://t.me/{username_bot}?start={user_id}'

    await bot.answer_callback_query(call.id, f"🫂")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=fich(f"""
                                    <b>[🫂] Реферальная программа <i>{name_bot}</i>
                                    
                                    <blockquote>📊 Ваша статистика:
                                    
                                    💵 Баланс: <code>{db.get_ref_balance(user_id)}$</code>
                                    🔎 Кол-во рефералов: <code>{db.count_referals(user_id)} чел.</code>
                                    📌 Реф.Процент: <code>5%</code>
                                    <a href='{url_link}'>📍 Ваша реферальная ссылка</a></blockquote></b>"""),
                                    reply_markup=back_in_profile())
    

@dp.callback_query_handler(text='out_ref_balance')
async def call_out_ref(call: types.CallbackQuery):

    user_id = call.from_user.id 

    balance = db.get_ref_balance(user_id)

    if balance > 0:
        await bot.answer_callback_query(call.id,f"✅ Ваш баланс поставлен на выплату! Обратитесь к владельцу", show_alert=True)
        db.minus_ref_balance(balance, user_id)

        user_link = f'<a href="tg://user?id={user_id}"><b>Аккаунт</b></a>'
        await bot.send_message(
                            chat_id=channel_info,
                            text=fich(f"""  
                            <b>💸 Новая выплата в казино!
                            🔎 Реферальная выплата!</b>
                                      
                            <b>💰 Сумма: {balance}$
                            👤 {user_link}</b>"""))
    else:
        await bot.answer_callback_query(call.id,f"❌ Ваш баланс равен 0!", show_alert=True)