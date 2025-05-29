from aiogram.utils import executor
import logging
from create_bot import dp, bot
from bot.handlers import dp 
from bot.misc.function import startup_sinca

async def on_start(_):
    print("[START] ----- Script Casino started...")
    startup_sinca()
    dp

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
