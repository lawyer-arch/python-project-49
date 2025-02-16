# ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ
from brain_games.worcer import progression_string, not_correct_answer


# Правила игры
RULES='What number is missing in the progression?'


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
    