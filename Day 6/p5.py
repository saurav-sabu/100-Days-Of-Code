# Python Program to Read a Number n and Compute n+nn+nnn


n = int(input("Enter the number to find n+nn+nnn:"))
temp = str(n)
t1 = temp+temp
t2 = temp+temp+temp
print("Calculate:",n+int(t1)+int(t2))