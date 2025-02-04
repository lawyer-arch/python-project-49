
### Импортируем библиотеки
from random import randint, choice
from random import randint
import prompt



### Генерируем случайное члисло
def rendom_number():
    random_number = randint(0, 100)
    return random_number

### Генератор случайных операторов

def operator():
    seg = ['+', '-', '*']
    operator = random.choice(seg)
    return operator

### Приветствие начало игры.

def welcome_user():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name