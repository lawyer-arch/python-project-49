from brain_games.cli1 import welcome_user, random_number
import sys
import math



def c_brain_gcd():
    name = welcome_user()  # Сохраняем имя
    print('Find the greatest common divisor of given numbers.')
    
    i = 0
    while i < 3:
        x = random_number()
        y = random_number()
                
        print(f'Question: {x} {y}')
        answer = input('Your answer: ')
        
        result = math.gcd(x, y)  # Вычисляем правильный ответ
        
        if result == int(answer):  # Приводим ответ пользователя к числу
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {result}.\n Let's try again, {name}!")
            sys.exit(0)
    
    print(f'Congratulations, {name}!')
