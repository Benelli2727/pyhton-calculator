n = int(input("Press(1) for adding, (2) for subtracting, (3) for multiplying and (4) for dividing"))
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
if(n==1):
    print(add(num1, num2))

if(n==2):
    print(subtract(num1,num2))

if(n==3):
    print(multiply(num1, num2))

if(n==4):
    print(divide(num1, num2))
