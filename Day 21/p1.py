# Python Program to Flatten a Nested List


l1 = [[1], [2, 3], [4, 5, 6, 7]]
final_list = []

for i in l1:
    for j in i:
        final_list.append(j)


print(final_list)