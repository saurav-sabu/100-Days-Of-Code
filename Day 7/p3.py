# Python Program to Check If Two Numbers are Amicable Numbers or Not

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

s1 = []
s2 = []

for i in range(1,num1):
    if num1%i == 0:
        s1.append(i)

for i in range(1,num2):
    if num2%i == 0:
        s2.append(i)


if num1 == sum(s2) and num2 == sum(s1):
    print(f"{num1} and {num2} are Amicable Numbers")
else:
    print(f"{num1} and {num2} are not Amicable Numbers")
