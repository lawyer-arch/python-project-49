# ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ
from brain_games.utils import not_correct_answer, progression
from random import randint


# Правила игры
RULES = 'What number is missing in the progression?'

# Создаем строку алгеброической прогресии с неизвестным элементом
def progression_string():
    temporary_list = list(map(str, progression(10)))
    ind = randint(1, len(temporary_list) - 1)
    simbol = temporary_list[ind]
    temporary_list[ind] = '..'
    temporary_string = ' '.join(temporary_list)  # Преобразуем список в строку
    print(f'Question: {temporary_string}')  # Выводим строку с прогрессией
    return simbol  # Возвращаем символ

def game_logic_progression(name):
    # Выводим на печать прогрессию и сохраняем тайную переменную 
    result = progression_string()  
    # Предлагаем ввести ответ
    answer = input('Your answer: ')

    # Вводим условия сравнения ответа        
    if int(result) == int(answer):  # Приводим ответ пользователя к числу
        print('Correct!')
        return True
    else:
        not_correct_answer(answer, result, name)
        return False  # Ответ неверный, прерываем игру
    