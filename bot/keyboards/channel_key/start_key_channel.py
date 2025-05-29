from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def channel_keyboard_stavka():
    s = InlineKeyboardMarkup()
    s1 = InlineKeyboardButton('💎 Играть', url="http://t.me/send?start=IVlx4ylj9608") # Поставишь сюда url для оплаты счета
    s.add(s1)
    return s 