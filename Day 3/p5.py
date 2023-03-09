# Python Program to Find the Gravitational Force between Two Objects

m1 = float(input("Enter mass of object 1:"))
m2 = float(input("Enter mass of object 2:"))
d = float(input("Enter distance between object 1 and object 2:"))
G = 6.67 * (10**-11)
f = (G*m1*m2)/(d**2)

print(f"Gravitational Force:",f)

