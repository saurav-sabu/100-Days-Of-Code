# Python Program to Count the Number of Words and Characters in a String

# method 1
sentence = input("Enter a sentence:").strip()

count_char = 0 

for i in sentence:
    count_char+=1

print("Number of Words:",len(sentence.split()))
print("Number of Characters:",count_char)

# method 2
sentence = input("Enter a sentence:").strip()

count_char = 0 
word = 1

for i in sentence:
    count_char+=1
    if i == " ":
        word+=1

print("Number of Words:",word)
print("Number of Characters:",count_char)
