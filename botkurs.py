import telebot
from telebot import types

bot = telebot.TeleBot('6810744108:AAFqvDZShGyGEqJuFlTT44RT-D4sd0b2aDA')


def knopka():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    som = types.KeyboardButton('Доллар ➡️ Сум')
    dollar = types.KeyboardButton('Сум ➡️ Доллар')
    kb.add(som, dollar)
    return kb


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Добро пожаловать на обмен валют.\n'
                              'Выберите какую валюту перевести.', reply_markup=knopka())


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    if message.text == 'Доллар ➡️ Сум':

        bot.register_next_step_handler(message, perevod_deneg)
    elif message.text == 'Сум ➡️ Доллар':
        bot.send_message(user_id, 'Введите сумму в сумах для перевода в доллары')
        qwerty(message)
    else:
        bot.send_message(user_id, 'Пожалуйста, выберите один из вариантов в меню.')


def perevod_deneg(message):
    user_id = message.from_user.id
    slova = message.text
    bot.send_message(user_id, 'Введите сумму в долларах для перевода в сум')
    bot.register_next_step_handler(message, convert_sum_dol)
def convert_sum_dol(message):
    user_id = message.from_user.id
    number = int(message.text)
    bot.send_message(user_id, f"Конвертация: {number*12000} SUM")
    # is_number = True
    # for alpha in slova:
    #     if alpha not in '0123456789':
    #         is_number = False
    #         break
    # if is_number:
    #     tsifra = int(slova)
    #     result = tsifra * 12500
    #     bot.send_message(user_id, result)
    #
    # else:
    #     bot.send_message(user_id, 'Я вас не понимаю, пока что это недоступно1')


def qwerty(message):
    user_id = message.from_user.id
    text = message.text
    if text.lower() == 'сум ➡️ доллар':
        bot.send_message(user_id, 'Введите сумму которую хотите перевести на Американских Доллоров2')
    else:
        bot.send_message(user_id, 'Я вас не понимаю, пока что это недоступно2')


bot.infinity_polling()
