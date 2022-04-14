from aiogram import types
from aiogram.dispatcher.filters import Command
from googletrans import Translator

from loader import dp

translator = Translator()

@dp.message_handler(Command("en", prefixes="!/"))
async def to_eng(message: types.Message):
	uz = message.text[4:]

	eng = translator.translate(uz, src='auto', dest="en")
	word = eng.text
	await message.reply(f"{word}")
	print(message.text)
	print(word)

@dp.message_handler(Command("ru", prefixes="!/"))
async def to_eng(message: types.Message):
	uz = message.text[4:]

	eng = translator.translate(uz, src='auto', dest="ru")
	word = eng.text
	await message.reply(f"{word}")
	print(message.text)
	print(word)

@dp.message_handler(Command("uz", prefixes="!/"))
async def to_eng(message: types.Message):
	uz = message.text[4:]

	eng = translator.translate(uz, src='auto', dest="uz")
	word = eng.text
	await message.reply(f"{word}")
	print(message.text)
	print(word)




#
# uz = message.text
#
# 	eng = translator.translate(uz, src='auto', dest="en")
# 	word = eng.text
# 	await message.reply(f"{word}")
# 	print(message.text)
# 	print(word)