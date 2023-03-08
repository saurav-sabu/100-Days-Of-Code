# Python Program to Count the Number of Digits Present In a Number

# method 1
num = int(input("Enter the number to find the number of digits:"))

lst = []
s = 0
while num!=0:
    s = num%10
    lst.append(s)
    num = num//10

print("Number of digits:",len(lst))

# method 2
num = input("Enter the number to find the number of digits:")
print("Number of digits:",len(num))