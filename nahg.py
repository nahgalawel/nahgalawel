 import telebot
from telebot import types


bot_token = '6127541125:AAFOb-tK-BS8md1aUb4CNlAUMQhK3ASNRAw'


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_command(message):
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='افتح الرابط', url='https://www.experai.com/chat?search=NahgAlawelGPT')
    markup.add(btn)
    # إرسال رسالة ترحيبية مع الزر
    bot.send_message(chat_id=message.chat.id, text='مرحباً بك في البوت الخاص بي!', reply_markup=markup)

bot.polling()