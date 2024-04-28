# importiruem bibleotek telebot, predvaritelno skachav ee cherez terminal "pip install telebot"
import telebot
from telebot import types
# sozdaem obyekt nashego bota (mozg bota)
bot = telebot.TeleBot('6809709837:AAHaCVrWZXy0bqtUHXcfIcVVQXQBrwQvvs8')

def knopka():
    #sozdaem prostranstva dlya knopki
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)    #(row_width=True)
    # sozdaem knopki
    knopka_perevodchik = types.KeyboardButton('nu blya')
    knopka_project = types.KeyboardButton('project')

    kb.add(knopka_perevodchik, knopka_project)
    return kb

# @bot.message_handler() - dekorator kotoriy slujit dlya obrobotki tex ili inix soobsheniy
#@bot.message_handler(content_types=['text'])
#def hello(message):
##    print(message.from_user.first_name)
#    print(message.from_user.id)
 #   print(message.from_user.username)
  #  print(message.from_user.language_code)
   # user_id = message.from_user.id
    #bot.send_message((user_id), 'hi hitler')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'qq epta', reply_markup=knopka())

@bot.message_handler(content_types=['text'])
def texting(message):
    user_id = message.from_user.id
    text = message.text
    if text.lower() == 'переводчик':
        bot.send_message(user_id, 'Vvedite slova dlya perevoda')
    else:
        bot.send_message(user_id, 'Ya vas ne ponimayu')
# dekoratr dlya reagirovanie na fotagrafii otpravlenie polzovatelya
@bot.message_handler(content_types=['photo'])
def send_photo(message):
    #poluchaem id polzavatelya
    user_id = message.from_user.id
    #soxronyaem url fotogrfagii
    photo = 'https://images.pexels.com/photos/607812/pexels-photo-607812.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
    # otpravlyaem foto polzavatelya
    bot.send_photo(user_id, photo, caption="eto telefon")





bot.infinity_polling() # bot.polling(non_stop=True)


