                                         ###ИГРА АЛГЕБРОИЧЕСКАЯ ПРОГРЕССИЯ####
from brain_games.cli1 import welcome_user
from brain_games.game_core_brain_progression import progression_string
import sys




def brain_progression():

    mystery_variable = progression_string() # тайная переменная
    name = welcome_user()  # Сохраняем имя
    print('What number is missing in the progression?')
    
    i = 0
    while i < 3:
        ### печатаем строку с алгеброической прогрессией
        print(progression_string)
        ### Предлагаем ввести ответ
        answer = input('Your answer: ')

        # вводим условия сравнения ответа        
        if mystery_variable == int(answer):  # Приводим ответ пользователя к числу
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {result}.\n Let's try again, {name}!")
            sys.exit(0)
    
    print(f'Congratulations, {name}!')

def main():
    welcome_user()
    brain_progression()    

if __name__ == "__main__":
    main()