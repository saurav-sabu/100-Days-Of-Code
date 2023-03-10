# Python Program to Replace All Occurrences of ‘a’ with $ in a String

# method 1

str1 = input("Enter the string:")

print("Original String:",str1)
print("Modified String:",str1.replace("a","$").replace("A","$"))

# method 2

str1 = input("Enter the string:")
s = ""

for i in str1:
    if i == "a" or i=="A":
        s+="$"
    else:
        s+=i
        

print("Original String:",str1)
print("Modified String:",s)