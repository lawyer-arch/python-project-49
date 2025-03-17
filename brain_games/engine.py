from brain_games.utils import welcome_user, conclusion_congratulations


NUM_OF_ROUNDS = 3


def c_brain_games(rules_of_the_game, game_logic_func):
    name = welcome_user()  # Сохраняем имя пользователя
    print(rules_of_the_game)

    for i in range(NUM_OF_ROUNDS):
        if game_logic_func(name):  # Вызываем переданную функцию
            i += 1
        else:
            return  # Завершаем игру при неправильном ответе

    conclusion_congratulations(name)
