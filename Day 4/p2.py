# Python Program to Remove the nth Index Character from a Non-Empty String

str1 =input("Enter the string:")
index = int(input("Enter the index to remove that character:"))
s = ""

for i in range(len(str1)):
    if index == i:
        continue
    else:
        s+=str1[i]

print("String:",s)