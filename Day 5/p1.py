# Python Program to Sort Words in Alphabetic Order

str1 = input("Enter the string to sort words in alphabetical order:").lower()

str1 = str1.split()
str1 = sorted(str1)
str1 = " ".join(str1)

print("Sorted String:",str1)

