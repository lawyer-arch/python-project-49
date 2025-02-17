# Импортируем библиотеки
from brain_games.worcer import random_number, not_correct_answer
import math

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'


def game_logic_gcd(name):
    x = random_number()
    y = random_number()
                
    print(f'Question: {x} {y}')
    answer = input('Your answer: ')
        
    result = math.gcd(x, y)  # Вычисляем правильный ответ
        
    if result == int(answer):  # Приводим ответ пользователя к числу
        print('Correct!')
        return True
    else:
        not_correct_answer(answer, result, name)
        return False  # Ответ неверный, прерываем игру
