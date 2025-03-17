from random import randint
import prompt


START_RANGE = 0
MIN_LIMIT_RANGE = 10
LIMIT_RANGE = 100


# Приветствие и запрос имени
def welcome_user():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# Запрос ответа пользователя и вывод ответ
def user_response():
    answer_user = input('Your answer: ')
    return answer_user


# Поздравление с удачным завершением игры
def congratulations(name):
    print(f'Congratulations, {name}!')


# В играх calc, gcd в случае не корректного
# ответа выводит информацию об этом.
def not_correct_answer(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was {result}. "
f"Let's try again, {name}!")
   

# В играх even, prime в случае не 
# корректного ответа выводит информацию об этом.
def not_correct_answer_even(name):
    print(f"'yes' is wrong answer ;(. Correct answer was 'no'. "
f"Let's try again, {name}!")
   

# Проверяем натуральность числа
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


# Создаем алгеброическу прогрессию
def progression(progression_length):
    d = randint(START_RANGE, MIN_LIMIT_RANGE)
    a = randint(START_RANGE, LIMIT_RANGE)
    result = []
    result.append(a)  # записываем первый симвло
    
    for i in range(0,progression_length):     
        new_row = result[i] + d  # создаем временную переменную
        result.append(new_row)

    return result
