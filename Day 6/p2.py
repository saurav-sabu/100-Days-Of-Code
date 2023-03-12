# Python Program to Check if a Number is a Palindrome

num = int(input("Enter the number to check whether it is palindrome number:"))

temp = num
s,d = 0,0
while num!=0:
    d = num%10
    s = s*10+d
    num = num//10

if temp == s:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")