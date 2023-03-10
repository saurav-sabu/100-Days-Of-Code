# Python Program that Displays Letters that are not Common in Two Strings


str1 = set(input("Enter the first string:"))
str2 = set(input("Enter the second string:"))

print("Letters that are not Common in Two Strings:",str1.symmetric_difference(str2))