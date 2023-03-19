# Python Program to Find Fibonacci Numbers using Recursion

n = int(input("Enter the number of terms to find fibonacci:"))

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


for i in range(1,n+1):
    print(fibo(i),end=" ")