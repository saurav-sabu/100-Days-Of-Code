# Python Program to Return the Length of the Longest Word from the List of Words

lst = ["Bangalore","Mumbai","Delhi"]

temp = len(lst[0])
max = lst[0]

for i in range(len(lst)):
    for j in range(i+1):
        if temp < len(lst[j]):
            temp = len(lst[j])
            max = lst[j]


print(f"Longest word is {max} and length of that word is {temp}")
