### Импортируем библиотеки
from random import randint
import sys
import prompt



### Генерируем случайное члисло
def rendom_number():
    random_number = randint(0, 100)
    return random_number

### Тело игры.
def c_brain_even():
    
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer = ''
    i = 0
    while i < 3:
        number = rendom_number()
        print(f'Question: {number}')
        print('Your answer: ', end='')
        answer = input()
        if number % 2 == 0 and answer == 'yes':
            print('Correct!')
            i += 1
        elif number % 2 != 0 and answer == 'no':
            print('Correct!')
            i += 1
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!''')
            sys.exit(0) 
    print(f'Congratulations, {name}!')