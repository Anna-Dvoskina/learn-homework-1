"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(FirstWord, SecondWord):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not(type(FirstWord) == str and type(SecondWord) == str):
        print(0)
    elif FirstWord == SecondWord:
        print(1)
    elif FirstWord != SecondWord and len(FirstWord) > len(SecondWord):
        print(2)
    elif FirstWord != SecondWord and 'learn' in FirstWord.lower():
        print(3)

if __name__ == "__main__":
    main(FirstWord = 5, SecondWord = 4)
    main(FirstWord = 'Python', SecondWord = 'Python')
    main(FirstWord = 'Python', SecondWord = 'Learn')
    main(FirstWord = 'Learn', SecondWord = 'Python')
