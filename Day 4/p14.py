# Python Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order

str1 = "Bangalore-hyderabad-delhi"

new_str = str1.split("-")
new_str = sorted(new_str)
new_str = "-".join(new_str)

print("Original String:",str1)
print("New String:",new_str)