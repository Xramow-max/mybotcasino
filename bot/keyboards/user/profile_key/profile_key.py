from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_profile_key():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('[🚀] Реф.Программа', callback_data='referal_program')
    s2 = InlineKeyboardButton('[💰] Пополнение', callback_data='add_balance')
    s3 = InlineKeyboardButton('[💸] Вывести', callback_data='dell_balance')
    s4 = InlineKeyboardButton('⬅️ Назад', callback_data='back_in_start')
    s.add(s1, s2)
    s.add(s3)
    s.add(s4)
    return s 

def back_in_profile():
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('[💸] Вывести', callback_data='out_ref_balance')
    s2 = InlineKeyboardButton('⬅️ Назад', callback_data='profile_user')
    s.add(s1)
    s.add(s2)
    return s 

def oplata_key(url):
    s = InlineKeyboardMarkup()

    s1 = InlineKeyboardButton('🔄 Оплатить', url=url)
    s.add(s1)
    return s 

def back_profile_go():
    s = InlineKeyboardMarkup()

    s2 = InlineKeyboardButton('⬅️ Назад', callback_data='profile_user')
    s.add(s2)
    return s 