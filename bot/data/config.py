import configparser
from aiocryptopay import AioCryptoPay

BOT_TOKEN = configparser.ConfigParser()
BOT_TOKEN.read("settings.ini")
BOT_TOKEN = BOT_TOKEN['settings']['token'].strip().replace(' ', '')

logs_id = -1002516596626 # Канал с логами
main_id = -1002532218096 # Основной канал с ставками
channel_info = -1002608461823 # Канал с выплатами

name_bot = 'PanWin Casino'
path = 'base.db'
username_bot = 'pantheonvin_Bot'

channel = "https://t.me/+fw6LpzwAurhjM2M6"
url_channel_main = 'https://t.me/+fw6LpzwAurhjM2M6'
url_support_main = 'https://t.me/WaltrWh1te'

crypto_bot_api = '373063:AA4dVjAkPS6kNbjUtb9n2NIT3hENscJTxyE' # api_key cryptobot
client = AioCryptoPay(token=crypto_bot_api)