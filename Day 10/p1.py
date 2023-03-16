# Python Program to find LCM of two numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a>b:
    g = a
else:
    g = b

for i in range(g,a*b+1):
    if i%a == 0 and i%b == 0:
        print(f"LCM of {a} and {b} is {i}")
        break