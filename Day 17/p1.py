''' Inverted half pyramid using *
* * * * *
* * * *
* * *
* *
* 

''' 

n = int(input("Enter the size n:"))

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()  