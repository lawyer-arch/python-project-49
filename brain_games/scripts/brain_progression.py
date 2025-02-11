# ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ
from brain_games.cli1 import welcome_user
from brain_games.games.game_core_brain_progression import progression_string
import sys


def brain_progression():
   
    name = welcome_user()  # Запускаем приветствие и сохраняем имя
    print('What number is missing in the progression?')
      
    i = 0
    while i < 3:
        # Выводим на печать прогрессию и сохраняем тайную переменную 
        mystery_variable = progression_string()  
        # Предлагаем ввести ответ
        answer = input('Your answer: ')

        # Вводим условия сравнения ответа        
        if int(mystery_variable) == int(answer):  # Приводим ответ пользователя к числу
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {mystery_variable}.\n Let's try again, {name}!")
            sys.exit(0)
    
    print(f'Congratulations, {name}!')


def main():
    brain_progression()    


if __name__ == "__main__":
    main()