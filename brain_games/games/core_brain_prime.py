# Импортируем библиотеки
from brain_games.utils import (is_prime,
                                error_output_even)
from random import randint


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Тело игры
def game_logic_prime(name):
    # Выводим на печать цифру и сохраняем ее в переменную 
    number = randint(START_RANGE, LIMIT_RANGE)
    print(f'Question: {number}')
    # Предлагаем ввести ответ
    answer = input('Your answer: ').strip().lower()

    is_number_prime = is_prime(number)    
    # Сравниваем ответ пользователя с результатом is_prime
    if (answer == 'yes') == is_number_prime:  
        print('Correct!')
        return True
    else:
        error_output_even(name)
        return False  # Ответ неверный, прерываем игру
