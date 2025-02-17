from brain_games.worcer import random_number, get_operator, user_response, not_correct_answer

RULES = 'What is the result of the expression?'


def game_logic_calc(name):  
    x = random_number()
    y = random_number()
    oper = get_operator()
    
    print(f'Question: {x} {oper} {y}')
    
    answer = user_response()  # Получаем ответ пользователя
    result = eval(f"{x} {oper} {y}")  # Вычисляем правильный ответ
    
    if result == int(answer):  
        print('Correct!')
        return True  # Ответ верный, продолжаем игру
    else:
        not_correct_answer(answer, result, name)
        return False  # Ответ неверный, прерываем игру
