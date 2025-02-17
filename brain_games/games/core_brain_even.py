# Импортируем библиотеки
from brain_games.worcer import random_number, get_operator, user_response, not_correct_answer_even


#Правила игры
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


# Тело игры.
def game_logic_even(name):
    number = random_number()
    print(f'Question: {number}')
    answer = user_response()  # Получаем ответ пользователя
    if number % 2 == 0 and answer == 'yes':
        print('Correct!')
        return True  # Ответ верный, продолжаем игру
    elif number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True  # Ответ верный, продолжаем игру
    else:
        not_correct_answer_even(name)
        return False  # Ответ неверный, прерываем игру