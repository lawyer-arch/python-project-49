from brain_games.worcer import welcome_user, congratulations


def c_brain_games(rules_of_the_game, game_logic_func):
    name = welcome_user()  # Сохраняем имя пользователя
    print(rules_of_the_game)

    i = 0
    while i < 3:
        if game_logic_func(name):  # Вызываем переданную функцию
            i += 1
        else:
            return  # Завершаем игру при неправильном ответе

    congratulations(name)
