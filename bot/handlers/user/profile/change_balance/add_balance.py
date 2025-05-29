# main
from create_bot import bot, dp 

from bot.data.db import Database
from bot.data.config import path
from bot.misc.filer import fich 
from bot.keyboards.user.profile_key.profile_key import back_profile_go 
from bot.misc.function_wallet import create_invoice, check_date_proverka
from bot.keyboards.user.profile_key.profile_key import oplata_key

# other
import base64
from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

db = Database(path)

class add_balance_state(StatesGroup):

    amount_value = State()

@dp.callback_query_handler(text='add_balance')
async def call_add_balance(call: types.CallbackQuery, state: FSMContext):

    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"💰")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=fich(f"""
                                    <b>[💰] Пополнение баланса
                                                
                                    [•] Система: <i>CryptoBot</i>
                                    [•] Минимальная сумма: <i>0.2$</i>
                                    [•] Баланс пополнится автоматически
                                                
                                    ✍🏻 Введите сумму к пополнению</b>"""),
                                    reply_markup=back_profile_go())
    await add_balance_state.amount_value.set()


@dp.message_handler(state=add_balance_state.amount_value)
async def message_add_balance(message: types.Message, state: FSMContext):

    user_id = message.from_user.id 
    message_id = message.message_id

    try:
        amount = float(message.text)
    except:
        await state.finish()
        with open('bot/photo/main.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] Не верный ввод суммы!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_profile_go())
        return
    
    if amount >= 0.2:
        await state.finish()
        sums = amount + (amount * 0.03)
        invoice = await create_invoice(sums)

        if invoice:

            url = invoice.bot_invoice_url  # Берем юрл для оплаты через бота из инвойма
            invoice_id = invoice.invoice_id  # Берем сам инвойс айди

            with open('bot/photo/main.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[✅]  Ваш счет создан!\n\n[•] Оплатите его и баланс зачислится автоматически!</b>",
                                        reply_markup=oplata_key(url))
                
            if await check_date_proverka(invoice_id):
                
                db.plus_balance(amount, user_id)
                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[💸] Ваш баланс успешно пополнен!\n\n[•] Для возврата нажмите на кнопку ниже!</b>",
                                        reply_markup=back_profile_go())

            else:
                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[ℹ️] Истек срок оплаты!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                        reply_markup=back_profile_go())

        else:
            await state.finish()
            with open('bot/photo/main.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[ℹ️] Произошла ошибка!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                        reply_markup=back_profile_go())

    else:
        await state.finish()
        with open('bot/photo/main.jpg', 'rb') as photo:
            await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] Минимальная сумма: <i>0.2$</i>!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_profile_go())