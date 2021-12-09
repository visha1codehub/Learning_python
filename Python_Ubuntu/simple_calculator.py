# take input to ask for operation
# take input two numbers
# operation

def add_num(a,b):
    return a+b

def subtract_num(a,b):
    return a-b

def multiply_num(a,b):
    return a*b

def divide_num(a,b):
    return a/b


while True:
    operation = input("Choose 'a' for Addition, 's' for Subtraction, 'm' for Multiplication, 'd' for division:-->").lower()
    num1 = int(input("Enter your 1st number:\n"))
    num2 = int(input("Enter your 2nd  number:\n"))
    if operation == 'a':
        print(add_num(num1,num2))
    elif operation == 's':
        print(subtract_num(num1,num2))
    elif operation == 'm':
        print(multiply_num(num1,num2))
    elif operation == 'd':
        print(divide_num(num1,num2))
    
        
