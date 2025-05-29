# main
from create_bot import bot, dp 

from bot.data.db import Database
from bot.data.config import path
from bot.keyboards.user.game_key.game_key import back_in_game, back_in_slot

# other
import base64
import asyncio
from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

db = Database(path)

class game_slot_state(StatesGroup):

    amount_value = State()

@dp.callback_query_handler(text='slot_game', state='*')
async def call_slot_game(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"🎰")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=f"<b>[ℹ️] Введите сумму ставки!\n\n[•] Ваша ставка: 🎰 Слоты\n[•] Баланс: {db.get_balance(user_id)}$</b>",
                                   reply_markup=back_in_game())
    await game_slot_state.amount_value.set()


@dp.message_handler(state=game_slot_state.amount_value)
async def message_game_slot(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
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
                                    reply_markup=back_in_slot())
            return
        
        if amount >= 0.2:
            if float(db.get_balance(user_id)) >= amount:
                await state.finish()
                
                db.minus_balance(amount, user_id)
                db.plus_turnover(amount, user_id)
                db.plus_games(user_id)

                slot = await bot.send_message(chat_id=user_id, text=f"<b>✅ Игра начата</b>")
                dc = await bot.send_dice(user_id, emoji='🎰', reply_to_message_id=slot.message_id)
                result = dc.dice.value

                await asyncio.sleep(2)

                if result in {6, 11, 16, 17, 27, 32, 33, 38, 54, 48, 49, 59}:
                    new_kef = 1.8
                    amount_win = amount * new_kef
                    
                    db.plus_balance(amount_win, user_id)

                    with open('bot/photo/main.jpg', 'rb') as photo:
                        await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[🏆] Победа! Вы выиграли <i>{round(amount_win,2)}$</i>!\n\n[⚡️] Вернитесь назад и сыграйте еще раз!</b>",
                                        reply_markup=back_in_slot())
                elif result in {1, 22, 43}:
                    new_kef = 2.8
                    amount_win = amount * new_kef
                    
                    db.plus_balance(amount_win, user_id)

                    with open('bot/photo/main.jpg', 'rb') as photo:
                        await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[🏆] Победа! Вы выиграли <i>{round(amount_win,2)}$</i>!\n\n[⚡️] Вернитесь назад и сыграйте еще раз!</b>",
                                        reply_markup=back_in_slot())
                elif result == 64:
                    new_kef = 5
                    amount_win = amount * new_kef
                    
                    db.plus_balance(amount_win, user_id)

                    with open('bot/photo/main.jpg', 'rb') as photo:
                        await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[🏆] Победа! Вы выиграли <i>{round(amount_win,2)}$</i>!\n\n[⚡️] Вернитесь назад и сыграйте еще раз!</b>",
                                        reply_markup=back_in_slot())
                else:
                    await state.finish()
                    with open('bot/photo/main.jpg', 'rb') as photo:
                        await bot.send_photo(chat_id=user_id,
                                        photo=photo,
                                        caption=f"<b>[😔] Поражение! Вы проиграли <i>{amount}$</i>!\n\n[⚡️] Вернитесь назад и сыграйте еще раз!</b>",
                                        reply_markup=back_in_slot())
                    
            else:
                await state.finish()
                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] На балансе недостаточно средств!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_in_slot())
        else:
            await state.finish()
            with open('bot/photo/main.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] Минимальная ставка <i>0.2$</i>!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_in_slot())

