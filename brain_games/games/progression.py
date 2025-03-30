# ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ
from random import randint

START_RANGE = 0
MIN_LIMIT_RANGE = 10
LIMIT_RANGE = 100

# Правила игры
RULES = 'What number is missing in the progression?'


# Создаем алгеброическу прогрессию
def making_progression(progression_length):
    d = randint(START_RANGE, MIN_LIMIT_RANGE)
    a = randint(START_RANGE, LIMIT_RANGE)
    result = []
    result.append(a)  # записываем первый симвло
    for i in range(0, progression_length):     
        new_row = result[i] + d  # создаем временную переменную
        result.append(new_row)
    return result


# Создаем строку алгеброической прогресии с неизвестным элементом
def progression_string():
    temporary_list = list(map(str, making_progression(MIN_LIMIT_RANGE)))
    ind = randint(1, len(temporary_list) - 1)
    simbol = temporary_list[ind]
    temporary_list[ind] = '..'
    temporary_string = ' '.join(temporary_list)  # Преобразуем список в строку
    return temporary_string, simbol  # Возвращаем символ


def game_logic_progression():
    question, correct_answer = progression_string()  
    return question, correct_answer
    