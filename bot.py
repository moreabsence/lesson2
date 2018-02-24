import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

from ephem import *

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

def main():
    updater = Updater("504744759:AAFLDudnlMRy7yyp196gpyAqQtbdntWEwkw")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("update", update))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet))
    updater.start_polling()
    updater.idle()

main()


