### Импортируем библиотеки
from brain_games.cli1 import welcome_user
from random import randint
import prompt
import sys


### Генерируем случайное члисло
def rendom_number():
    random_number = randint(0, 100)
    return random_number


### Проверяем натуральность числа
def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True
 

###################################Игра "Простое число"######################################

def brain_prime_start():

    name = welcome_user()  # Запускаем приветствие и сохраняем имя
    # Предлагаем варианты ответа
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0
    while i < 3:
        # Выводим на печать цифру и сохраняем ее в переменную 
        number = rendom_number()
        print(f'Question: {number}')
        # Предлагаем ввести ответ
        answer = input('Your answer: ')
        
        if is_prime(number) == True and answer == 'yes':
            print('Correct!')
            i += 1
        elif is_prime(number) == False and answer == 'no':
            print('Correct!')
            i += 1
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!''')
            sys.exit(0)

    print(f'Congratulations, {name}!')
