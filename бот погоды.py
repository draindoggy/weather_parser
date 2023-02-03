from telebot import types
import telebot
import weather_parser

bot = telebot.TeleBot('токен')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('погода в Москве')
    btn2 = types.KeyboardButton('погода в Санкт-Петербурге')
    btn3 = types.KeyboardButton('погода в Новосибирске')
    btn4 = types.KeyboardButton('погода в Екатеринбурге')
    btn5 = types.KeyboardButton('погода в Казани')
    btn6 = types.KeyboardButton('погода в Нижнем Новгороде')
    btn7 = types.KeyboardButton('погода в Челябинске')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, text='''привет, {0.first_name}! 
я погодный бот. выбери на кнопке город, и я пришлю тебе температуру в этом городе!'''.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'погода в Москве':
        bot.send_message(message.from_user.id, text=weather_parser.text1)
    elif message.text == 'погода в Санкт-Петербурге':
        bot.send_message(message.from_user.id, text=weather_parser.text2)
    elif message.text == 'погода в Новосибирске':
        bot.send_message(message.from_user.id, text=weather_parser.text3)
    elif message.text == 'погода в Екатеринбурге':
        bot.send_message(message.from_user.id, text=weather_parser.text4)
    elif message.text == 'погода в Казани':
        bot.send_message(message.from_user.id, text=weather_parser.text5)
    elif message.text == 'погода в Нижнем Новгороде':
        bot.send_message(message.from_user.id, text=weather_parser.text6)
    elif message.text == 'погода в Челябинске':
        bot.send_message(message.from_user.id, text=weather_parser.text7)

bot.infinity_polling()
