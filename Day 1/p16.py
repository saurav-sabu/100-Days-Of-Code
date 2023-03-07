# Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N


num = int(input("Enter the value of N:"))
sum = 0

for i in range(1,num+1):
    sum += (1/i)

print(f"Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/{num} is {sum}")