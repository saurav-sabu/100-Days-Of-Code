# Python Program to Solve Quadratic Equation

print("Form of Quadratic Equation ax²+bx+c=0")
a = int(input("Enter the coefficient of a:"))
b = int(input("Enter the coefficient of b:"))
c = int(input("Enter the coefficient of c:"))

D = (b**2) - (4*a*c)

if D>0:
    print("real roots")
    r1 = (-b + (D**0.5))/2*a
    r2 = (-b - (D**0.5))/2*a
    print(f"Roots are {r1} and {r2}")
elif D == 0:
    print("One Real root")
    r1 = (-b + (D**0.5))/2*a
    print(f"Roots are {r1}")
else:
    print("We get complex number")
    r1 = (-b + (D**0.5))/2*a
    r2 = (-b + (D**0.5))/2*a
    print(f"Roots are {r1} and {r2}")
