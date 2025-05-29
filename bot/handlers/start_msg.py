# bot
from create_bot import bot, dp 
from bot.misc.filer import IsPrivate, fich
import bot.misc.function as functions
from bot.data.config import name_bot

from bot.keyboards.admin.start_admin_panel import start_keyboard_admin
from bot.keyboards.user.user_key import start_user_keyboard

# module 
from aiogram import types 
import base64


@dp.message_handler(IsPrivate(), commands=['start'])
async def start_message_(message: types.Message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username 
    
    start_command = message.text

    if await functions.check_database_user(first_name, username, user_id, start_command): # Добавление пользователя в бд при необходимости
        if functions.is_admin(user_id): # Проверка на администратора 
                with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(
                        chat_id=user_id,
                        photo=photo,
                        caption=fich(f"""
                        <b>🎲 Добро пожаловать в {name_bot}
                        
                        ⚡️ Вы вошли в админ панель</b>"""),
                        reply_markup=start_keyboard_admin()
                    )


        else:
            with open('bot/photo/main.jpg', 'rb') as photo:
                    await bot.send_photo(
                        chat_id=user_id,
                        photo=photo,
                        caption=fich(f"""<b>🎲 Добро пожаловать в {name_bot}</b>"""),
                        reply_markup=start_user_keyboard()
                    )

@dp.callback_query_handler(text='back_in_start')
async def call_back_in_start(call: types.CallbackQuery):
     
    user_id = call.from_user.id 
    message_id = call.message.message_id

    await bot.answer_callback_query(call.id, f"⬅️ Назад")
    if functions.is_admin(user_id): # Проверка на администратора 
        await bot.edit_message_caption(
            chat_id=user_id,
            message_id=message_id,
            caption=fich(f"""
            <b>🎲 Добро пожаловать в {name_bot}
                        
            ⚡️ Вы вошли в админ панель</b>"""),
            reply_markup=start_keyboard_admin()
            )


    else:
        await bot.edit_message_caption(
            chat_id=user_id,
            message_id=message_id,
            caption=fich(f"""<b>🎲 Добро пожаловать в {name_bot}</b>"""),
            reply_markup=start_user_keyboard()
            )