# Python Program to Create a New String Made up of First and Last 2 Characters

str1 = input("Enter the string:")

new_str = str1[:2] + str1[-2:]

print("Original String:",str1)
print("New String:",new_str)