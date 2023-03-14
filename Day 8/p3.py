# Python Program to Split Even and Odd Elements into Two Lists

lst = [23,44,99]

lst_even = [x for x in lst if x%2==0]
lst_odd = [x for x in lst if x%2!=0]

print("Even numbers:",lst_even)
print("Odd numbers:",lst_odd)