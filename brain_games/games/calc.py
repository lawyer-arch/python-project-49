from brain_games.utils import user_response, error_output
from random import randint, choice

OPERATORS = ('+', '-', '*')
START_RANGE = 0
LIMIT_RANGE = 100
RULES = 'What is the result of the expression?'


def game_logic_calc():  
    x = randint(START_RANGE, LIMIT_RANGE)
    y = randint(START_RANGE, LIMIT_RANGE)
    oper = choice(OPERATORS)  # Получаем случайынй опервтор
    
    question = f'{x} {oper} {y}'
    
    correct_answer = eval(question)  # Вычисляем правильный ответ

    return question, correct_answer
