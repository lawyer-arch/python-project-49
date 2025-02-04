from brain_games.scripts.cli1 import welcome_user
from brain_games.scripts.cli1 import rendom_number
from brain_games.scripts.cli1 import operator
from brain_games.scripts.cli1 import name
import sys

def brain_calc():
    
    print('What is the result of the expression?')
    answer = ''
    i = 0
    while i < 3:
        x = rendom_number()
        y = rendom_number()
        oper = operator()
        print(f'Question: {x} {oper} {y}')
        print('Your answer: ', end='')
        answer = input()
        if f'{x} {oper} {y}' == answer:
            print('Correct!')
            i += 1
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '175'. Let's try again, Sam!''')
            sys.exit(0) 
    print(f'Congratulations, {name}!')

def main():
    welcome_user()
    brain_calc()    


if __name__ == "__main__":
    main()