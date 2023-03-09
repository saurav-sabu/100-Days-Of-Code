# Python Program to Count the Number of Digits and Letters in a String

str1 = input("Enter the string to count Number of Digits and Letter:")
dcount,lcount = 0,0

for i in str1:
    if i.isdigit():
        dcount+=1
    if i.isalpha():
        lcount+=1

print("Number of digits in string:",dcount)
print("Number of letters in string:",lcount)