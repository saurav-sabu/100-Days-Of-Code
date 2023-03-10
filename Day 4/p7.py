# Python Program to Check if the Substring is Present in the Given String

str1 = input("Enter the string:")
substr = input("Enter the sub string:")

if str1.find(substr) == -1:
    print(f"{substr} is not present in string {str1}")
else:
    print(f"{substr} is present in string {str1}")
    
