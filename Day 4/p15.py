# Python Program to Count the Occurrences of Each Word in a String

str1 = input("Enter the string to count the occurance of word:").strip().split()

d = {}

for i in str1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1


print("Count of each word in string:",d)