"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

answers = {
    "Как дела?": "Хорошо!", 
    "Что делаешь?": "Программирую",
    "Какой язык программирования ты учишь?": "Python",
    "Какую тему ты сейчас изучаешь?": "Оператор While"
}
def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """

    user_question = input("Спроси меня что-нибудь: ")
    answer = answers.get(user_question)
    if answer:
        print(answer)
    else:
        print('Спроси меня что-нибудь другое')    

if __name__ == "__main__":
    ask_user(answers)
