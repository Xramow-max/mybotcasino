from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard_admin():
    s = InlineKeyboardMarkup()
    s1 = InlineKeyboardButton('[💰] Казна', callback_data='kazna')
    s2 = InlineKeyboardButton('[💼] Профиль', callback_data='profile_user')
    s3 = InlineKeyboardButton('[📊] Статистика', callback_data='statistic')
    s4 = InlineKeyboardButton('[📚] Информация', callback_data='info_user')
    s.add(s2)
    s.add(s1, s3)
    s.add(s4)
    return s 

def back_in_panel_adm():
    s = InlineKeyboardMarkup()
    s1 = InlineKeyboardButton('⬅️ Назад', callback_data='kazna_back')
    s.add(s1)
    return s 