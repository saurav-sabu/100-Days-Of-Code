# Python Program to Swap Two Variables

# first method 

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Before Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)
print()
num1,num2 = num2,num1
print()
print("After Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)

# second method

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Before Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)
print()

temp = num1
num1 = num2
num2 = temp

print()
print("After Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)

# third method

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("Before Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)
print()

num1 = num1 + num2   # 10 + 20 = 30
num2 = num1 - num2   # 30 - 20 = 10
num1 = num1 - num2   # 30 - 10 = 20

print()
print("After Swapping:")
print(f"Value of first number:",num1)
print(f"Value of second number:",num2)

