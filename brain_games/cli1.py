from random import randint, choice
import prompt


# Генерируем случайное число
def random_number():
    return randint(0, 100)


# Генерируем случайный оператор
def get_operator():
    seg = ['+', '-', '*']
    return choice(seg)


# Приветствие и запрос имени
def welcome_user():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
