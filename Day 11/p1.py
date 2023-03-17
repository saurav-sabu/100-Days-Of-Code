# Python Program to print Fibonacci Series

n = int(input("How many numbers of fibonacci Series to print:"))

a,b = 0,1

if n>=2:
    print(a,b,end=" ")
    for i in range(n-2):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
