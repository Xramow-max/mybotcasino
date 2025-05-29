from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from create_bot import bot, dp 
from aiogram.dispatcher.filters import BoundFilter

# Удаление отступов у текста
def fich(get_text: str) -> str:
    if get_text is not None:
        split_text = get_text.split("\n")

        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)
    else:
        get_text = ""

    return get_text

class IsPrivate(BoundFilter):
    async def check(self, message):
        if "id" in message:
            return message.message.chat.type == types.ChatType.PRIVATE
        else:
            return message.chat.type == types.ChatType.PRIVATE