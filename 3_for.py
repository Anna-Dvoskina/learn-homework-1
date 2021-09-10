"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

students_score = [
  {'school_class': '4a', 'scores': [3,4,4,5,2]},
  {'school_class': '4б', 'scores': [5,4,5,2,4]},
  {'school_class': '4в', 'scores': [2,3,2,3,2]},
  {'school_class': '4г', 'scores': [4,5,4,5,5]},
  {'school_class': '4д', 'scores': [1,2,4,5,3]},
]
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    score_in_school = 0
    number_of_scores_in_school = 0
    for classes in students_score:
        score_in_class = 0 
        number_of_scores = 0 
        for scores in classes['scores']:
            score_in_class += scores
            number_of_scores += 1
        print(f'Средняя оценка по клаасу {classes["school_class"]}: {score_in_class/number_of_scores}')
        score_in_school += score_in_class
        number_of_scores_in_school += number_of_scores
    print(f'Средняя оценка по школе: {score_in_school/number_of_scores_in_school}')
    
if __name__ == "__main__":
    main()

