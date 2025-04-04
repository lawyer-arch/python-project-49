from random import randint, choice

OPERATORS = ('+', '-', '*')
START_RANGE = 0
LIMIT_RANGE = 100
RULES = 'What is the result of the expression?'


def evaluate_expression(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        return num1 * num2
    

def calculate_operation():  
    num1 = randint(START_RANGE, LIMIT_RANGE)
    num2 = randint(START_RANGE, LIMIT_RANGE)
    operation = choice(OPERATORS)
    
    question = f'{num1} {operation} {num2}'
    
    correct_answer = evaluate_expression(num1, num2, operation)

    return question, correct_answer
