import telebot
from telebot import types
token = "6548731888:AAFJH1hwf6_toOXWgTsR2saQFjnrSdA1Prk"
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте, я ваше персональное расписание, пропишите (Расписание) чтобы получить информацию о парах")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(commands=['Расписание',])
def start(massage):
	markup_inline = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text = 'Расписание', callback_data = 'rasp')
item2 = types.InlineKeyboardButton(text = 'Информация', callback_data = 'info')
markup_inline.add(item1,item2)
bot.send_massage(message.chat.id, 'Что хотите узнать?',
	reply_markup = markup_inline
)



bot.infinity_polling()