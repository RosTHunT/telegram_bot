import telebot
from telebot import types

bot = telebot.TeleBot('5568316033:AAHCk6D47d6pKmSrWGE-NeVNEBgqyS-H6BU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
#
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'Привіт', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твій id: {message.from_user.id}', parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('img_2.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Команду не знайдено', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'хороше фото!')


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('веб сайт')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'перейти на сайт', reply_markup=markup)


bot.polling(none_stop=True)