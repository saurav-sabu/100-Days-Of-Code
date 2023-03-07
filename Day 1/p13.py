# Python Program to Find the Factorial of a Number

num = int(input("Enter the number to find factorial:"))
fact = 1

for i in range(1,num+1):
    fact = fact * i

print(f"Factorial of {num} is {fact}")