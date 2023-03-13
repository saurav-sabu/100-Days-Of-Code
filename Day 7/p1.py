# Python Program to Find All the Divisors of an Integer

num = int(input("Enter the number to find divisor:"))

for i in range(1,num+1):
    if num%i == 0:
        print(i)