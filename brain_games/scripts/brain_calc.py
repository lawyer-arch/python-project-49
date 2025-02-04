from cli1 import welcome_user
from cli1 import rendom_number
from cli1 import operator
from cli1 import name
import sys

def brain_calc():
    welcome_user()
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
        result = eval(f"{x} {oper} {y}")

        if result == answer:
            print('Correct!')
            i += 1
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was {result}. Let's try again, {name}!''')
            sys.exit(0) 
    print(f'Congratulations, {name}!')

def main():
    brain_calc()    


if __name__ == "__main__":
    main()