from telegram import Update, BotCommandScopeDefault, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json


def hello(bot, context: CallbackContext) -> None:
    response_API = requests.get('https://random.dog/woof.json')
    data = response_API.text
    parse_json = json.loads(data)['url']
    bot.message.reply_text(f'Держи, {bot.effective_user.first_name} {parse_json}', reply_markup=markup)


updater = Updater('5190624076:AAHA2aZZZagd74CsdP26_0N960cS3Cd9w5E')

updater.dispatcher.add_handler(CommandHandler('more', hello))
reply_keyboard=[['/more',]]
markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
updater.start_polling()
updater.idle()