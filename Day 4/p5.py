# Python Program to Count the Number of Vowels in a String

str1 = input("Enter the string to find vowel:")
vowel = ["a","e","i","o","u","A","E","I","O","U"]
count = 0

for i in str1:
    if i in vowel:
        count+=1

print("Number of vowels:",count)