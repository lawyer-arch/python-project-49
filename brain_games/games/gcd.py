# Импортируем библиотеки
from brain_games.utils import error_output
from random import randint
import math


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'


def game_logic_gcd(name):
    x = randint(START_RANGE, LIMIT_RANGE)
    y = randint(START_RANGE, LIMIT_RANGE)
    question = x, y          
    correct_answer = math.gcd(x, y)  # Вычисляем правильный ответ
    return question, correct_answer
