# Python Program to Find the Sum of Natural Numbers

num = int(input("Enter the value of n:"))
sum = 0

if num<0:
    print("Positive number")
else:
    for i in range(1,num+1):
        sum += i

    print(f"Sum of {num} natural number is",sum)