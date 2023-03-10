# Python Program to Find Common Characters in Two Strings

str1 = set(input("Enter the first string:"))
str2 = set(input("Enter the second string:"))

print("Common Characters in string:",str1.intersection(str2))