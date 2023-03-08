# Python Program to Trim Whitespace From a String

# method 1
num = input("Enter the string to remove whitespaces:")
s = ""
for i in num:
    if i!=" ":
        s+=i

print(s)

# method 2

num = input("Enter the string to remove whitespaces:")

print(num.strip())