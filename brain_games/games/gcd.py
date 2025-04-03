# Импортируем библиотеки
from random import randint
import math


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'


def find_the_divisor():
    num1 = randint(START_RANGE, LIMIT_RANGE)
    num2 = randint(START_RANGE, LIMIT_RANGE)
    question = f'{num1} {num2}'
    correct_answer = math.gcd(num1, num2)  # Вычисляем правильный ответ
    return question, correct_answer
