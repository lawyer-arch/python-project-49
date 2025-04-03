# ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ
from random import randint

START_RANGE = 0
MIN_LIMIT_RANGE = 10
LIMIT_RANGE = 100

# Правила игры
RULES = 'What number is missing in the progression?'


# Создаем алгеброическу прогрессию
def make_progression(progression_length):
    num1 = randint(START_RANGE, MIN_LIMIT_RANGE)
    num2 = randint(START_RANGE, LIMIT_RANGE)
    result = []
    result.append(num2)  # записываем первый симвло
    for i in range(0, progression_length):     
        new_row = result[i] + num1  # создаем временную переменную
        result.append(new_row)
    return result


# Создаем строку алгеброической прогресии с неизвестным элементом
def get_progression_string():
    temporary_list = list(map(str, make_progression(MIN_LIMIT_RANGE)))
    ind = randint(1, len(temporary_list) - 1)
    correct_answer = temporary_list[ind]
    temporary_list[ind] = '..'
    question = ' '.join(temporary_list)  # Преобразуем список в строку
    return question, correct_answer  # Возвращаем строку и ответ
