# Python Program that Displays which Letters are in First String but not in Second

str1 = set(input("Enter the first string:"))
str2 = set(input("Enter the second string:"))

print("Letters are in First String but not in Second:",str1.difference(str2))