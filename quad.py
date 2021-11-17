import math
print("-----Quadratic Equation is in the form ax**2+bx+c, where a,b,c are constants.-----")
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))


dis=(b**2)-(4*a*c)

root1=(-b+math.sqrt(dis))/(2*a)
print("Root 1: ", root1)
root2=(-b-math.sqrt(dis))/(2*a)
print("Root 2: ", root2)
