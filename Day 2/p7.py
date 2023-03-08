# Python Program to Remove Duplicate Element From a List

# method 1
lst = [1,2,1,4,6]

lst_new = []

for i in lst:
    if i not in lst_new:
        lst_new.append(i)

print(lst_new)

# method 2
lst = [1,2,1,4,6]

print(list(set(lst)))

