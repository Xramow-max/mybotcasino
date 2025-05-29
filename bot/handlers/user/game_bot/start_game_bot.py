# main
from create_bot import bot, dp 

from bot.keyboards.user.game_key.game_key import start_game_keyboard 

# other
import base64
from aiogram import types 
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text='game_user', state='*')
async def call_game_user(call: types.CallbackQuery, state: FSMContext):

    await state.finish()
    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"🎲")
    await bot.edit_message_caption(chat_id=user_id,
                                   message_id=message_id,
                                   caption=f"<b>[ℹ️] Выберите игру для продолжения!</b>",
                                   reply_markup=start_game_keyboard())