# Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List

lst = [-45,-23,56,23,7]

s_even = 0
s_odd = 0
s_negative = 0

for i in lst:
    if i<0:
        s_negative+=i
    elif i>0:
        if i%2 == 0:
            s_even+=i
        else:
            s_odd+=i

print("Sum of Odd numbers:",s_odd)
print("Sum of Even numbers:",s_even)
print("Sum of Negative numbers:",s_negative)