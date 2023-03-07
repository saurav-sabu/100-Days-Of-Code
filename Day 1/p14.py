# Python Program to Display the multiplication Table

num = int(input("Enter the number to find multiplication table:"))

print(f"####### Multiplication Table of {num} #######")
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")