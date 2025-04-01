import prompt


NUM_OF_ROUNDS = 3


def user_response():
    answer_user = input('Your answer: ')
    return answer_user.lower()


def welcome_user():    
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def c_brain_games(rules_of_the_game, game_logic_func):
    name = welcome_user()
    print(rules_of_the_game)
    for i in range(NUM_OF_ROUNDS):
        question, correct_answer = game_logic_func()
        print(f'Question: {question}')
        answer = user_response()

        if str(correct_answer) == str(answer):
            print('Correct!')
                       
        else:
            print(f'{answer} is wrong answer ;(. ' 
                  f'Correct answer was {correct_answer}. '
                  f'Let\'s try again, {name}!'
            )
        
    print(f'Congratulations, {name}!')
