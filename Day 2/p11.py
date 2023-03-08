# Python Program to Get the File Name From the File Path

file_name = input("Enter File Name to extract extension:")
fname = file_name.split(".")[0]
ext = file_name.split(".")[1]
print(f"Extension of {fname} is {ext} ")
