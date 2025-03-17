# Импортируем библиотеки
from brain_games.worcer import not_correct_answer
from random import randint
import math


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'


def game_logic_gcd(name):
    x = randint(START_RANGE, LIMIT_RANGE)
    y = randint(START_RANGE, LIMIT_RANGE)
                
    print(f'Question: {x} {y}')
    answer = input('Your answer: ')
        
    result = math.gcd(x, y)  # Вычисляем правильный ответ
        
    if result == int(answer):  # Приводим ответ пользователя к числу
        print('Correct!')
        return True
    else:
        not_correct_answer(answer, result, name)
        return False  # Ответ неверный, прерываем игру
