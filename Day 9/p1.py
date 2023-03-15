# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

start = int(input("Enter the starting range:"))
end = int(input("Enter the ending range:"))

for i in range(start,end+1):
    if i%7 == 0 and i%5 ==0:
        print(i)