# Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!


num = int(input("Enter the value of N:"))
sum = 0
fact = 1

for i in range(1,num+1):
    fact = fact * i
    sum += (1/fact)

print(f"Sum of the Series 1/1!+1/2!+1/3!+…1/N! is {sum}")