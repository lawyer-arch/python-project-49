# Импортируем библиотеки
from random import randint


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# Тело игры.
def check_even():
    question = randint(START_RANGE, LIMIT_RANGE)
   
    if question % 2 == 0:
        return question, 'yes'
    else:
        return question, 'no'
    