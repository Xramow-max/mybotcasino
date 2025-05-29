from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_game_keyboard():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('[✌🏻] КНБ', callback_data='knb_game')
    s2 = InlineKeyboardButton('[🎰] Слоты', callback_data='slot_game')
    s3 = InlineKeyboardButton('⬅️ Вернуться', callback_data='back_in_start')
    s.add(s1,s2)
    s.add(s3)
    return s 

def start_knb_game():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('✊🏻', callback_data='knbplay_✊🏻')
    s2 = InlineKeyboardButton('✌🏻', callback_data='knbplay_✌🏻')
    s3 = InlineKeyboardButton('🤚🏻', callback_data='knbplay_🤚🏻')
    s4 = InlineKeyboardButton('⬅️ Вернуться', callback_data='game_user')
    s.add(s1,s2,s3)
    s.add(s4)
    return s 

def back_in_knb():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('⬅️ Вернуться', callback_data='knb_game')
    s.add(s1)
    return s 

def back_in_game():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('⬅️ Вернуться', callback_data='game_user')
    s.add(s1)
    return s 

def back_in_slot():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('🔄 Еще раз', callback_data='slot_game')
    s.add(s1)
    return s 