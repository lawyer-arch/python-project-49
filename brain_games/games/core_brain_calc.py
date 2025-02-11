from brain_games.cli1 import welcome_user, random_number, get_operator
import sys

def c_brain_calc():
    name = welcome_user()  # Сохраняем имя
    print('What is the result of the expression?')
    
    i = 0
    while i < 3:
        x = random_number()
        y = random_number()
        oper = get_operator()
        
        print(f'Question: {x} {oper} {y}')
        answer = input('Your answer: ')
        
        result = eval(f"{x} {oper} {y}")  # Вычисляем правильный ответ
        
        if result == int(answer):  # Приводим ответ пользователя к числу
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {result}.\n Let's try again, {name}!")
            sys.exit(0)
    
    print(f'Congratulations, {name}!')