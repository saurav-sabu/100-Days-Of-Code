# Python Program to Remove Odd Indexed Characters in a string

str1 = input("Enter the string:")
s = ""

for i in range(len(str1)):
    if i%2 == 0:
        s += str1[i]

print("Original String:",str1)
print("Transformed String:",s)

