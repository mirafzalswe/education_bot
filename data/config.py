from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qish uchun
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMIN = env.int("ADMIN")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
TEACHERS = env.list('TEACHERS') # Support Teacherlar uchun
