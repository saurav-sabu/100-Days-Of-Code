# Python Program to Find the GCD of Two Numbers

num1 = int(input("Enter the first number to find GCD:"))
num2 = int(input("Enter the second number to find GCD:"))

while num1%num2!=0:
    rem = num1%num2
    num1,num2 = num2,rem

print(f"HCF is {num2}")

