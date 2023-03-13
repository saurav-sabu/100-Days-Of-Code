# Python Program to Check Whether a Given Number is Perfect Number

num = int(input("Enter perfect number:"))
sum = 0 

for i in range(1,num):
    if num%i == 0:
        sum+=i        

if num == sum:
    print(f"{num} is Perfect number")
else:
    print(f"{num} is not a Perfect number")