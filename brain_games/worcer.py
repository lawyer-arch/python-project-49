from random import randint, choice
import prompt


# Генерируем случайное число
def random_number():
    random_number = randint(0, 100)
    return random_number


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


# Запрос ответа пользователя и вывод ответ
def user_response():
    answer_user = input('Your answer: ')
    return answer_user


# Поздравление с удачным завершением игры
def congratulations(name):
    print(f'Congratulations, {name}!')


# В играх calc, gcd в случае не корректного ответа выводит информацию об этом.
def not_correct_answer(answer, result, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was {result}. "
f"Let's try again, {name}!")
   

# В играх even, prime в случае не корректного ответа выводит информацию об этом.
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
def progression():
    d = randint(0, 10)
    a = randint(0, 100)
    result = []
    result.append(a)  # записываем первый симвло
    i = 0
    while i < 10:     
        new_row = result[i] + d  # создаем временную переменную
        result.append(new_row)  # записываем элементы прогресии
        i += 1  
    return result  # возвращаем строку-прогрессию


# Создаем строку алгеброической прогресии с неизвестным элементом
def progression_string():
    temporary_list = list(map(str, progression()))
    ind = randint(1, len(temporary_list) - 1)
    simbol = temporary_list[ind]
    temporary_list[ind] = '..'
    temporary_string = ' '.join(temporary_list)  # Преобразуем список в строку
    print(f'Question: {temporary_string}')  # Выводим строку с прогрессией
    return simbol  # Возвращаем символ
