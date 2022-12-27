import telebot
# Створюємо об'єкт бота
bot = telebot.TeleBot("5815303250:AAEyVTo1g1xwMO96NabBULGwiiOLXHD0-OA")
# Обробник повідомлень
@bot.message_handler(commands=["start"])
# Створюємо функцію обробника
def bot_start(message):
    # Відправник повідомлень
    bot.send_message(message.chat.id, "Hello, User!")
# Опитування всіх чатів
bot.polling()