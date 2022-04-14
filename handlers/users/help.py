from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>❗️Qo'llanma! 📝</b>\n",
            "Inglizchaga tarjima qilish uchun -- <b>/en</b> <i>so'z</i>",
            "Ruschaga tarjima qilish uchun -- <b>/ru</b> <i>so'z</i>",
            "O'zbekchaga tarjima qilish uchun -- <b>/uz</b> <i>so'z</i>\n\n"
            "Misol uchun:  /uz apple")

    await message.answer("\n".join(text))