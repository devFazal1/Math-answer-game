import random

TOTAL_QUESTIONS = 10
MIN_OPERAND = 3
MAX_OPERAND = 12
OPERATORS = ['+', '-', '*']

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + operator + str(right)
    result = eval(expr)
    
    return result, expr

wrong = 0 
correct = 0   
for i in range(TOTAL_QUESTIONS):
    result, expr = generate_problem()
    
    while True:
        user_response = input("Question no #"+ str(i+1)+ " " + expr+": ")
        if user_response == str(result):
            correct += 1
            break
        else:
            wrong += 1
            print(f"Wrong answer, Try again. Total wrong answers given: {wrong}")
            
        
print(f"Your score: {correct} correct answers, {wrong} wrong answers")
