# Импортируем библиотеки
from brain_games.worcer import is_prime, random_number, not_correct_answer_even


# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Тело игры
def game_logic_prime(name):
    # Выводим на печать цифру и сохраняем ее в переменную 
    number = random_number()
    print(f'Question: {number}')
    # Предлагаем ввести ответ
    answer = input('Your answer: ').strip().lower()

    is_number_prime = is_prime(number)    
    # Сравниваем ответ пользователя с результатом is_prime
    if (answer == 'yes') == is_number_prime:  
        print('Correct!')
        return True
    else:
        not_correct_answer_even(name)
        return False  # Ответ неверный, прерываем игру
