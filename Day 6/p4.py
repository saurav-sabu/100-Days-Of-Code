# Python Program to Find Sum of Digits of a Number

num = int(input("Enter the numebr to find sum of digit:"))
s,d = 0,0
temp = num

while num!=0:
    d = num%10
    s = s+d
    num = num//10

print(f"Sum of digits of number {temp}:",s)