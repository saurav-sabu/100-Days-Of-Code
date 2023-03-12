# Python Program to Print All Odd Numbers in a Range

start = int(input("Enter starting range:"))
end = int(input("Enter ending range:"))

for i in range(start,end+1):
    if i%2!=0:
        print(i)


