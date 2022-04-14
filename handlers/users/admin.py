from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from states.send_message_to_admin import SendMessage

from loader import dp, bot


@dp.message_handler(Command("admin"))
async def write_message(message: types.Message):
    await message.answer("Shikoyat va takliflarni shu yerga yozing ✍️ ...")

    await SendMessage.message.set()

@dp.message_handler(state=SendMessage.message)
async def send_messsage_to_admin(message: types.Message, state:FSMContext):
    await message.reply("✅ Xabaringiz muvaffaqiyatli adminga yuborildi. Botimizdan foydalanganingiz uchun tashakkur! 😊")
    sended_message = f"{message.text}\n\n{message.from_user.full_name} | {message.from_user.username}"
    await bot.send_message(chat_id=ADMINS[0], text=sended_message)

    await state.finish()