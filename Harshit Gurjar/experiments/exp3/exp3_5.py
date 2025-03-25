a=int(input("Enter the coefficient of x**2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant number: "))
if((b**2)-4*a*c>=0):
    print("The equation has real roots")
    root1= (-b+((b**2)-4*a*c)**0.5)/(2*a)
    root2= (-b-((b**2)-4*a*c)**0.5)/(2*a)
    print(f"the first root is {root1}")
    print(f"the second root is {root2}")
elif((b**2)-4*a*c<0):
    print("The equation has imaginary roots")
