# Python Program to Count Occurrences of Element in List

lst = [12,45,67,45,67,67,67]

d = {}
d = {}

for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1


print("Occurrences of Element in List:",d)