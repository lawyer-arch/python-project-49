from brain_games.utils import user_response, error_output
from random import randint, choice

OPERATORS = ('+', '-', '*')
START_RANGE = 0
LIMIT_RANGE = 100
RULES = 'What is the result of the expression?'


def game_logic_calc():  
    num1 = randint(START_RANGE, LIMIT_RANGE)
    num2 = randint(START_RANGE, LIMIT_RANGE)
    operation = choice(OPERATORS)  # Получаем случайынй опервтор
    
    question = f'{num1} {operation} {num2}'
    
    correct_answer = eval(question)  # Вычисляем правильный ответ

    return question, correct_answer
