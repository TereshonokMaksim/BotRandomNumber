import telebot

# ідентифікатори повідомлень
# message.from_user.first_name - перше ім'я користувача (ім'я)
# message.from_user.last_name - друге ім'я користувача (прізвище)
# message.from_user.username - псевдонім користувача
# message.text - отримати текст з посилання

# Створюємо об'єкт бота
bot = telebot.TeleBot("5815303250:AAEyVTo1g1xwMO96NabBULGwiiOLXHD0-OA")
# Обробник повідомлень

@bot.message_handler(commands=["start", "hello"])
# Створюємо функцію обробника
def bot_start(message):
    # Відправник повідомлень
    bot.send_message(message.chat.id, "Hello, User! My name is IntensiveRandomBot!")
    bot.register_next_step_handler(message, all_commands)
#
@bot.message_handler(commands= ["Hi"])
def bot_hello(message):
    bot.send_message(message.chat.id, f"Nice, to meet you! {message.from_user.username}!")
# 
def all_commands(message):
    if message.text.lower() == "play":
        bot.send_message(message.chat.id, "Game started!")
        bot.register_next_step_handler(message, all_commands)

# Опитування всіх чатів
bot.polling()