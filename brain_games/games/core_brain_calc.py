from brain_games.utils import (user_response,
                                not_correct_answer)
from random import randint, choice

OPERATORS = ('+', '-', '*')
START_RANGE = 0
LIMIT_RANGE = 100
RULES = 'What is the result of the expression?'


def game_logic_calc(name):  
    x = randint(START_RANGE, LIMIT_RANGE)
    y = randint(START_RANGE, LIMIT_RANGE)
    oper = choice(OPERATORS) # Получаем случайынй опервтор
    
    print(f'Question: {x} {oper} {y}')
    
    answer = user_response()  # Получаем ответ пользователя
    result = eval(f"{x} {oper} {y}")  # Вычисляем правильный ответ
    
    if result == int(answer):  
        print('Correct!')
        return True  # Ответ верный, продолжаем игру
    else:
        not_correct_answer(answer, result, name)
        return False  # Ответ неверный, прерываем игру
