# Python Program to Find the Length of a String without Library Function

str1 = input("Enter the string to find length:")
count = 0

for i in str1:
    count+=1

print(f"Length of string {str1} is {count}")