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
import copy
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
        update.message.reply_text(f'{count} слова')
    

def calc(update, context):
    user_text = update.message.text
    numbers = re.split('\s*[*+-/]\s*', user_text[6:])
    if not re.findall('\d+[*+-/]\d+', user_text[6:]): 
        update.message.reply_text('Может ты ввел лишние пробелы? Или ты написал цифры прописью?')
    else:
        x = int(numbers[0])
        y = int(numbers[1])
        z = re.findall('[*+-/]', user_text[6:])
        def calcfunc(x,y,z):
            if not(x, y):
                return 'нет цифр'
            if z == ['*']:
                return x*y
            elif z == ['-']:
                return x-y
            elif z == ['+']:
                return x+y
            elif z == ['/']:
                try:
                    return x/y
                except ZeroDivisionError:
                    return update.message.reply_text('Делить на ноль нельзя') 
        update.message.reply_text(calcfunc(x,y,z))             

def myname(update, context):
    username = update.message.chat.username
    update.message.reply_text(username)

total_cities = [
'Moscow', 'NewYork', 'Berlin', 'Paris', 'Deli', 'Istanbul', 'Ankara', 'TelAviv', 'Shanghai',
'Beijing', 'Vienna', 'Sofia', 'Havana', 'Athens', 'Tbilisi', 'Riga', 'Limassol'
]

def cities_game(update, context):

    username = update.message.chat.username
    all_cities = copy.copy(total_cities)
    users_cities = {username: all_cities}
    user_text = update.message.text.split()

    if len(user_text) == 1:
        update.message.reply_text('Напиши название города!')
    else:
        city =  user_text[1]
        if city in users_cities[username]:
            last_letter = city[-1]
            users_cities[username].remove(city)

            count = 0
            for new_city in users_cities[username]:
                if new_city[0].lower() == last_letter:
                    count += 1
                    update.message.reply_text(new_city) 
                    users_cities[username].remove(new_city)
                    break
            if count == 0: 
                update.message.reply_text('Больше городов на эту букву нет')
               
        else:
            update.message.reply_text('Я не знаю такого города')                        
                

        # cities_for_game = all_cities

def main():
    mybot = Updater("1940519188:AAFtdXOZrb8j8PydiGJphA6UdWAfE05TBr0", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("myname", myname))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("moon", moon))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(CommandHandler("city", cities_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
