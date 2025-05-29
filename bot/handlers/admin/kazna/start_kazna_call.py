#bot
from create_bot import bot, dp 
from bot.misc.filer import fich 
from bot.data.config import client, name_bot
import bot.misc.function as functions
from bot.keyboards.admin.start_admin_panel import back_in_panel_adm, start_keyboard_admin

#module 
import base64
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class add_kazna_state(StatesGroup):

    amount_add = State()


@dp.callback_query_handler(text='kazna', state='*')
async def admin_kazna_call(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id
    message_id = call.message.message_id

    if await functions.get_balance_kazna() == 'Не найден токен!':
        await bot.answer_callback_query(call.id, f"‼️ Не найден токен!", show_alert=True)
    else:
        await bot.answer_callback_query(call.id, text="💰 Казна")
        await bot.edit_message_caption(chat_id=user_id,
                                    message_id=message_id,
                                    caption=fich(f"""
                                    <b>Баланс: <code>{await functions.get_balance_kazna()}$</code>
                                    
                                    Введите сумму для пополнения казны в $:</b>
                                    """),
                                    reply_markup=back_in_panel_adm())
        await add_kazna_state.amount_add.set()


@dp.message_handler(state=add_kazna_state.amount_add)
async def amount_add_msg(message: types.Message, state: FSMContext):

    user_id= message.from_user.id
    message_id = message.message_id

    async with state.proxy() as data:

        try:
            amount = float(message.text)
        except:
            await bot.send_message(user_id, f"<b>Введите число!</b>",
                                   reply_markup=back_in_panel_adm())
            return 
        
        answ = await client.create_invoice(asset='USDT', amount=amount)

        url_bot = answ.bot_invoice_url
        mini_ap = answ.mini_app_invoice_url

        await bot.send_message(user_id, f"<a href='{url_bot}'>Пополнение URL</a>\n<a href='{mini_ap}'>Mini App</a>",
                               reply_markup=back_in_panel_adm())
        await state.finish()
        



@dp.callback_query_handler(text='kazna_back', state='*')
async def back_kazn(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"⬅️ Назад")
    await bot.edit_message_caption(
            chat_id=user_id,
            message_id=message_id,
            caption=fich(f"""
            <b>🎲 Добро пожаловать в {name_bot}
                        
            ⚡️ Вы вошли в админ панель</b>"""),
            reply_markup=start_keyboard_admin()
            )