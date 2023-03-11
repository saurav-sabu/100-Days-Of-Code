# Python Program to Check if a Key is Already Present in a Dictionary

key = input("Check whether Key is Already Present in a Dictionary:")

d = {"a":1,"b":2,"c":3,"d":4}

if key in d:
    print("Key is present")
else:
    print("Key is not present")