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
import re

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
    update.message.reply_text('Привет!')

def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)

def planet(update, context):
    try:
        user_text = update.message.text.split()
        planet = getattr(ephem, user_text[1])()
        planet.compute(ephem.Date(current_date))
        const = ephem.constellation(planet)
        update.message.reply_text(const)
    except AttributeError:
        update.message.reply_text('Такую планету еще не открыли')   


def moon(update, context):
    
    user_text = update.message.text.split()
    if len(user_text) == 1:
        update.message.reply_text('Привет! Напиши дату в формате 2021-09-11')
    else:    
        date = user_text[1]
        moon = ephem.next_full_moon(date)
        update.message.reply_text(moon)

def wordcount(update, context):
    user_text = update.message.text
    if len(user_text.split()) == 1: 
        update.message.reply_text('Пустая строка')
    else:
        count = 0 
        words_to_count = re.split('\s*[;,.\s]\s*', user_text)
        for word in words_to_count[1:]:
            if re.match( '\d+', word) or re.match( '[!?]', word):
                count = count
            else:
                count += 1    
        update.message.reply_text(count)
    
        # words_to_count = words_to_count[1:]
        # len_words_to_count = len(words_to_count)  
        # update.message.reply_text(len_words_to_count)



all_cities = ['Moscow', 'NewYork', 'Kazan', 'Novgorod', 'Kiev', 'Deli', 'Vladivostok', 'Krasnoyarsk']

def cities_game(update, context):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        update.message.reply_text('Привет! Напиши название города!')
    else:
        city =  user_text[1]
        if city in all_cities:
            last_letter = city[-1]
            all_cities.remove(city)
            for new_city in all_cities:
                if new_city[0].lower() == last_letter.lower():
                    update.message.reply_text(new_city) 
                    all_cities.remove(new_city)
                    break
                # else:
                #     update.message.reply_text(f'на букву {last_letter} больше городов нет')
                #     break 
        else:
            update.message.reply_text('Такого города я не знаю')                        
                

        # cities_for_game = all_cities




def main():
    mybot = Updater("1940519188:AAFtdXOZrb8j8PydiGJphA6UdWAfE05TBr0", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("moon", moon))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("city", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
