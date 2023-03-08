# Python Program to Reverse a Number

# method 1
num = int(input("Enter the number to reverse:"))

rev,s = 0,0
temp = num
while num!=0:
    s = num%10
    rev = rev*10 + s
    num = num//10

print(f"Reverse of {temp} is {rev}")

# method 2
num = input("Enter the number to reverse:")
print(f"Reverse of {num} is {num[::-1]}")