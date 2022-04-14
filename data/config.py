# from environs import Env
#
# # Теперь используем вместо библиотеки python-dotenv библиотеку environs
# env = Env()
# env.read_env()
#
# BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
# ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
#


from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili