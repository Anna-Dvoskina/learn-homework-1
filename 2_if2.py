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
def compare_strings(first_word, second_word):
    if not(isinstance(first_word, str) or isinstance(second_word, str)):
        print(0)
    elif first_word == second_word:
        print(1)
    elif first_word != second_word and len(first_word) > len(second_word):
        print(2)
    elif first_word != second_word and 'learn' in first_word.lower():
        print(3)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    compare_strings(first_word = 5, second_word = 4)
    compare_strings(first_word = 'Python', second_word = 'Python')
    compare_strings(first_word = 'Python', second_word = 'Learn')
    compare_strings(first_word = 'Learn', second_word = 'Python')


if __name__ == "__main__":
    main()
