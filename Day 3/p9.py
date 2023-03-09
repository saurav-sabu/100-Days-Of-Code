# Python Program to Replace Every Blank Space with Hyphen in a String

# method 1

str1 = input("Enter the string:")

print("Original String:",str1)
print("Replaced String:",str1.replace(" ","-"))


# method 2

str1 = input("Enter the string:")
s = ""

for i in str1:
    if i == " ":
        s+="-"
    else:
        s+=i

print("Original String:",str1)
print("Replaced String:",s)