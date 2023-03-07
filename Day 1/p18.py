# Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n

x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
sum = 1

for i in range(2,n+1):
    sum += (x**i)/i

print(f"Sum of the Series: 1 + x^2/2 + x^3/3 + … x^n/n is {sum}")