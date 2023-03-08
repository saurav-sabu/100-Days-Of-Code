# Python Program to Print all Prime Numbers in an Interval

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

for i in range(start,end+1):
    if i == 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(f"{i} is a prime number")