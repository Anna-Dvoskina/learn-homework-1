"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

current_date = (datetime.date(datetime.now()))

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text('Привет! Напиши название планеты в формате: /planet Mars')


def talk_to_me(update, context):
    try:
        user_text = update.message.text.split()
        planet = getattr(ephem, user_text[1])()
        planet.compute(ephem.Date(current_date))
        const = ephem.constellation(planet)
        print(const)
        update.message.reply_text(const)
    except AttributeError:
        print(update.message.reply_text('Такую планету еще не открыли'))    

def moon(update, context):
    
    user_text = update.message.text.split()
    if len(user_text) == 1:
        update.message.reply_text('Привет! Напиши дату в формате 2021-09-11')
    else:    
        update.message.reply_text(user_text[1])
        # moon = ephem.next_full_moon(date)

def main():
    mybot = Updater("1940519188:AAFtdXOZrb8j8PydiGJphA6UdWAfE05TBr0", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("moon", moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
