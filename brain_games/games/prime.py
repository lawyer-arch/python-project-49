# Импортируем библиотеки
from brain_games.utils import (is_prime, error_output_even)
from random import randint


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Тело игры
def game_logic_prime(name):
    question = randint(START_RANGE, LIMIT_RANGE)
    correct_answer = is_prime(question)    
    if correct_answer:
        return question, 'yes'  
    else:
        return question, 'no'
