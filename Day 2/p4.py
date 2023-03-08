# Python Program to Check 3 digit Armstrong Number

num = int(input("Enter the number to check whether it is armstrong number or not:"))
s,d = 0,0
temp = num
while num!=0:
    d = num%10
    s = s+d*d*d
    num = num//10

if temp == s:
    print(f"{temp} is armstrong number")
else:
    print(f"{temp} is not armstrong number")