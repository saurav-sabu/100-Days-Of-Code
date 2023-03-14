# Python Program to Find Largest Number in a List


# method 1

lst = [34,56,24,54]

temp = lst[0]

for i in range(len(lst)):
    for j in range(i+1):
        if lst[j]>temp:
            temp = lst[j]

print("Largest Number in List:",temp)

# method 2

lst = [34,56,24,54]

print("Largest Number in List:",sorted(lst)[-1])