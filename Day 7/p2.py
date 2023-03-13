# Python Program to Find the Smallest Divisor of an Integer

num = int(input("Enter the Smallest Divisor of an Integer:"))

for i in range(2,num+1):
    if num%i == 0:
        print("Smallest divisor:",i)
        break


