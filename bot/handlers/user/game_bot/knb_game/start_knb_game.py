# main
from create_bot import bot, dp 

from bot.data.db import Database
from bot.data.config import path
from bot.keyboards.user.game_key.game_key import start_knb_game, back_in_knb

# other
import base64
import random
import asyncio
from aiogram import types 
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

db = Database(path)

class game_knb_state(StatesGroup):

    value_amount = State()

def forrmated_name_stavka(emoji):
    if emoji == '✊🏻':
        return '✊🏻 Камень'
    elif emoji == '✌🏻':
        return '✌🏻 Ножницы'
    elif emoji == '🤚🏻':
        return '🤚🏻 Бумага'

@dp.callback_query_handler(text='knb_game', state='*')
async def call_knb_game(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"✌🏻")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=f"<b>[ℹ️] Выберите вашу ставку!\n\n[•] Игра: ✌🏻 КНБ\n[•] Суть игры: <i>Обычная игра камень\ножницы\бумага.</i></b>",
                                   reply_markup=start_knb_game())
    


@dp.callback_query_handler(Text(startswith='knbplay'))
async def call_knbplay(call: types.CallbackQuery, state: FSMContext):

    user_id = call.from_user.id 
    message_id = call.message.message_id

    data = call.data.split('_')
    emoji = data[1]

    await bot.answer_callback_query(call.id, f"{emoji}")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=f"<b>[ℹ️] Введите сумму ставки!\n\n[•] Ваша ставка: <i>{forrmated_name_stavka(emoji)}</i>\n[•] Баланс: <i>{db.get_balance(user_id)}$</i></b>",
                                   reply_markup=back_in_knb())
    await game_knb_state.value_amount.set()
    async with state.proxy() as data:
        data['emoji'] = emoji


@dp.message_handler(state=game_knb_state.value_amount)
async def message_game_balance(message: types.Message, state: FSMContext):

    user_id = message.from_user.id 
    message_id = message.message_id

    async with state.proxy() as data:
        emojis = data.get('emoji')

        try:
            amount = float(message.text)
        except:
            await state.finish()
            with open('bot/photo/main.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] Не верный ввод суммы!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_in_knb())
            return
        
        if amount >= 0.2:
            if float(db.get_balance(user_id)) >= amount:
                await state.finish()

                db.minus_balance(amount, user_id)
                db.plus_turnover(amount, user_id)
                db.plus_games(user_id)

                await bot.send_message(chat_id=user_id, text=f"<b>✅ Игра начата</b>")
                await bot.send_message(chat_id=user_id, text=f'{emojis}')

                if emojis == '🤚🏻':
                    bot_choice = random.choice(['✊🏻', '✌🏻'])
                elif emojis == '✊🏻':
                    bot_choice = random.choice(['✌🏻', '🤚🏻'])
                elif emojis == '✌🏻':
                    bot_choice = random.choice(['✊🏻', '🤚🏻'])

                await asyncio.sleep(0.9)
                
                await bot.send_message(chat_id=user_id, text=f"{bot_choice}")

                win_map = {
                    '🤚🏻': '✊🏻',
                    '✊🏻': '✌🏻',
                    '✌🏻': '🤚🏻',
                }

                if emojis == bot_choice:
                    result = "[🤝] Ничья! Ваш баланс возвращен!"
                    db.plus_balance(amount, user_id)
                elif win_map[emojis] == bot_choice:
                    koef = amount * 1.8
                    db.plus_balance(koef, user_id)
                    result = f"[🏆] Победа! Вы выиграли <i>{round(koef,2)}$</i>"
                else:
                    result = f"[😔] Поражение! Вы проиграли <i>{amount}$</i>"

                await asyncio.sleep(0.3)

                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>{result}!\n\n[⚡️] Вернитесь назад и сыграйте еще раз!</b>",
                                    reply_markup=back_in_knb())

            else:
                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] На балансе недостаточно средств!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_in_knb())
        else:
            with open('bot/photo/main.jpg', 'rb') as photo:
                await bot.send_photo(chat_id=user_id,
                                    photo=photo,
                                    caption=f"<b>[ℹ️] Минимальная ставка <i>0.2$</i>!\n\n[•] Вернитесь назад и попробуйте еще раз!</b>",
                                    reply_markup=back_in_knb())

