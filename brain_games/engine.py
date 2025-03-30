from brain_games.utils import welcome_user, conclusion_congratulations, user_response, error_output


NUM_OF_ROUNDS = 3


def c_brain_games(rules_of_the_game, game_logic_func):
    name = welcome_user()  # Сохраняем имя пользователя
    print(rules_of_the_game)
    

    for i in range(NUM_OF_ROUNDS):
        question, correct_answer = game_logic_func()
        print(f'Question: {question}')
        answer = user_response()

        if str(correct_answer) == str(answer):
            print('Correct!')
            i += 1
            
        else:
            error_output(answer, correct_answer, name) # Завершаем игру при неправильном ответе
            return
        
    conclusion_congratulations(name)
