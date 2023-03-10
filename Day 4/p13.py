# Python Program to Swap the First and the Last Character of a String

str1 = input("Enter the string to swap First and the Last Character:")

new_str = str1[-1] + str1[1:-1] + str1[0]

print("Original String:",str1)
print("New String:",new_str)