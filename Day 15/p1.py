''' Program to print half pyramid using *

*
* *
* * *
* * * *
* * * * *

'''

n = int(input("Enter the size of pyramid:"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()