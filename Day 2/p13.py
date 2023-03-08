# Python Program to Concatenate Two Lists

# method 1
lst1 = [1,2,3]
lst2 = [4,5,6]

print(lst1 + lst2)

# method 2
lst1 = [1,2,3]
lst2 = [4,5,6]
for i in lst2:
    lst1.append(i)

print(lst1)

# method 3
lst1 = [1,2,3]
lst2 = [4,5,6]

lst1.extend(lst2)

print(lst1)