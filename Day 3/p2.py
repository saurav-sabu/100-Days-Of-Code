# Python Program to Check If a String Is a Number (Float)

a = "1.123"

try:
    if type(float(a)) == float: 
        print("Yes it is a float number")
except Exception as e:
    print("It is not a float number")