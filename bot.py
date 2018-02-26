import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

from ephem import *

from collections import Counter

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    text = 'Привет дружок!'
    print(text)
    update.message.reply_text(text)

def update(bot, update):
    print(update)
    update.message.reply_text(update.to_dict())

def planet(bot, update):
    planet_name = (update.message.text)
    planet_name = planet_name.replace('/planet ', '') 
    print(planet_name)
    planets = {
    'Mercury' : Mercury,
    'Moon': Moon,
    'Venus': Venus,
    'Mars' : Mars, 
    'Jupiter' : Jupiter, 
    'Saturn' : Saturn, 
    'Uranus' : Uranus, 
    'Neptune' : Neptune, 
    'Pluto' : Pluto, 
    'Sun' : Sun, 
    'Moon' : Moon
    }
    m = planets.get(planet_name) 
    location = constellation(m('2018/2/23'))
    if planet_name in planets:
            update.message.reply_text(location)
    else:
            update.message.reply_text(planet_name)

def wordcount(bot, update):
    input_text = update.message.text
    input_text = input_text.replace('/wordcount', '')
    words = input_text.split()
    bad_words = ['.','?','!','&','*']
    for x in bad_words:
        if x in words:
            words.remove(x)
    words_sum = len(words)
    if words_sum == 0:
        update.message.reply_text('Вы забыли ввести слова. Бывает.')
    else:
        update.message.reply_text('{} слова'.format(words_sum))

def calculate(bot, update):
    calc_string = update.message.text
    if calc_string.endswith('='):
        calc_string = calc_string.replace('=', '')
        if '-' in calc_string:
            numbers = calc_string.split('-')
            result = float(numbers[0]) - float(numbers[1])
            update.message.reply_text(result)
        if '+' in calc_string:
            numbers = calc_string.split('+')
            result = float(numbers[0]) + float(numbers[1])
            update.message.reply_text(result)
        if '/' in calc_string:
            numbers = calc_string.split('/')
            second_number = numbers[1]
            if second_number.startswith ('0') and not '.' in second_number:
                update.message.reply_text('Я пока не умею делить на ноль.')    
            else:
                result = float(numbers[0]) / float(numbers[1])
                update.message.reply_text(result)
        if '*' in calc_string:
            numbers = calc_string.split('*')
            result = float(numbers[0]) * float(numbers[1])
            update.message.reply_text(result)
        if '**' in calc_string:
            numbers = calc_string.split('**')
            result = float(numbers[0]) ** float(numbers[1])
            update.message.reply_text(result)
    else:
        update.message.reply_text('Сама ты {}'.format(calc_string))


def main():
    updater = Updater("504744759:AAFLDudnlMRy7yyp196gpyAqQtbdntWEwkw")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("update", update))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('wordcount', wordcount))
    dp.add_handler(MessageHandler(Filters.text, calculate))
    updater.start_polling()
    updater.idle()

main()


