# Python Program to Find 3 digit Armstrong Number in an Interval

start = int(input("Enter the starting point:"))
end = int(input("Enter the ending point:"))


for i in range(start,end+1):
    s,d = 0,0
    temp = i
    while i!=0:
        d = i%10
        s = s+d*d*d
        i = i//10
    if temp == s:
        print(f"{temp} is armstrong number")
    