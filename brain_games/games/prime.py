# Импортируем библиотеки
from random import randint


START_RANGE = 0
LIMIT_RANGE = 100

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


# Тело игры
def prime_number_check():
    question = randint(START_RANGE, LIMIT_RANGE)
    return question, "yes" if is_prime(question) else "no"
