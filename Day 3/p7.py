# Python Program to Count Number of Lowercase Characters in a String

str1 = input("Enter the string to find number of lowercase:")
lower_count = 0

for i in str1:
    if i.lower() == i:
        lower_count +=1

print(f"Number of Lowercase Characters in string {str1} is {lower_count}")