# Python Program to Make a Simple Calculator

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

while True:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    choice = int(input("""Enter Operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Div
    5. Exit
    """))

    if choice == 1:
        print("Add:",add(a,b))
    elif choice == 2:
        print("Subtract:",subtract(a,b))
    elif choice == 3:
        print("Multiply:",multiply(a,b))
    elif choice == 4:
        print("Divide:",divide(a,b))
    elif choice == 5:
        exit(0)
    else:
        print("Wrong choice")