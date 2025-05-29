from bot.data.db import Database
from aiogram import types 
from bot.data.config import client, path
from create_bot import bot, dp
import base64

db = Database(path)

async def check_referal(start_command, user_id, username):

    """ Проверяем на реферала при старте """
    ref_id = str(start_command[7:])
    if ref_id != '':
        if str(ref_id) != str(user_id):
            db.add_user_ref(user_id, ref_id)
            try:
                await bot.send_message(ref_id, f"<b>[👤] Новый реферал! @{username}</b>")
            except:
                pass
        else:
            db.add_user_ref(user_id)
    else:
        db.add_user_ref(user_id)
    
    return True

async def check_database_user(first_name, username, user_id, start_command):

    """Функция при старте, для проверки существования юзера в базе данных"""

    if not db.user_exists(user_id):  # Если пользователя нету в базе данных
        await check_referal(start_command, user_id, username)
        db.add_user(first_name, username, user_id)
        return True

    else: # Если пользователь есть в базе данных
        return True
    

async def check_referal_payment(user_id, amount):

    ref_id_user = int(db.get_ref_id(user_id))
    ref_amount = round(float(amount) * 0.05, 1)
    db.plus_ref_balance(ref_amount, ref_id_user)
    try:
        await bot.send_message(ref_id_user, f"<b>💰 Ваш реф.баланс пополнен на <code>{ref_amount}$</code></b>")
    except Exception as e:
        print(e)
        pass

def is_admin(user_id):

    """Функция проверки на администратора"""

    with open('admins.txt', 'r') as file:
        admin_ids = file.read().splitlines()
    return str(user_id) in admin_ids


def startup_sinca():
    print("")


"""  Функции с документацией CryptoBot"""
    
async def get_balance_kazna():
    try:
        balances = await client.get_balance()

        # Ищем баланс для валюты USDT
        usdt_balance = next((balance for balance in balances if balance.currency_code == 'USDT'), None)

        if usdt_balance:
            # Возвращаем только доступный баланс
            return usdt_balance.available
        else:
            return 'Не найден токен!'

    except Exception as e:
        print(e)
        return 'Не найден токен!'