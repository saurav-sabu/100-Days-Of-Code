# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

start = int(input("Enter starting range:"))
end = int(input("Enter ending range:"))

for i in range(start,end+1):
    if i%2!=0 and i%3!=0:
        print(i)

