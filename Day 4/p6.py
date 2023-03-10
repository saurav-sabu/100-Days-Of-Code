# Python Program to Count Number of Uppercase and Lowercase Letters in a String

str1 = input("Enter the string:")
l_count = 0
u_count = 0

for i in str1:
    if i == i.lower():
        l_count+=1
    elif i == i.upper():
        u_count+=1

print("Number of Uppercase letters:",u_count) 
print("Number of Lowercase letters:",l_count) 