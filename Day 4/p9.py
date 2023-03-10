# Python Program to Print All Letters Present in Both Strings

str1 = set(input("Enter the first string:"))
str2 = set(input("Enter the second string:"))

print("All characters present in both strings:",str1.union(str2))