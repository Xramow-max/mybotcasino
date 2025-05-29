from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.data.config import url_channel_main, channel

def start_user_keyboard():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('[💼] Профиль', callback_data='profile_user')
    s2 = InlineKeyboardButton('[📚] Инфо', callback_data='info_user')
    s3 = InlineKeyboardButton('[🔎] Канал', url=channel)
    s4 = InlineKeyboardButton('[🎲] Игры', callback_data='game_user')
    s.add(s4)
    s.add(s2,s1)
    s.add(s3)
    return s

def back_in_start():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('⬅️ Назад', callback_data='back_in_start')
    s.add(s1)
    return s 