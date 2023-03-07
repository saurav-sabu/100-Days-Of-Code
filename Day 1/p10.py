# Python Program to Check if a Number is Positive, Negative or 0

num = int(input("Enter the number:"))
if num>0:
    print(f"{num} is positive")
elif num == 0:
    print(f"Number is zero")
else:
    print(f"{num} is negative")