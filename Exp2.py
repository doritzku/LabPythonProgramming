# Experiment 2 - by Ravi Ardhana 590013582 B-10
# Q1
x,y,z = 9,7,1
print(x+y+z)
print(x-y-z)
print(x*y*z)
print(x/y/z)

# Q2
radius = float(input("Enter radius:"))
pi = 3.141
area = pi*(radius*radius)
print(area,"sq. units")

# Q3
x = int(input("Enter x: "))
y = int(input("Enter y: "))
product = (x+y)*(x+y)
print(product)

# Q4
from math import sqrt
a = int(input("Enter length of perpendicular:"))
b = int(input("Enter length of base:"))
hypotenuse = ((a**2)+(b**2))**(1/2)
print(hypotenuse)

# Q5
p = int(input("Enter principle amount: "))
t = int(input("Enter time(in years): "))
i = float(input("Enter rate of interest: "))
s_i = (p*t*i)/100
print( (s_i))

# Q6
a = int(input("Enter length of first side : "))
b = int(input("Enter length of second side: "))
c = int(input("Enter length of third side: "))
s = (a+b+c)**(1/2)  # sqrt of perimeter of triangle 
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print((area))

# Q7
x = int(input("Enter seconds: "))
hours = x//(3600)
sec_left = x%3600
minutes= sec_left//60
seconds = sec_left%60
print(hours,"hours :",minutes,"minutes :",seconds,"seconds")

# Q8
a = 8
b = 4
# a,b = b,a
a = a+b
b= a-b
a= a-b
print(a,b)

# Q9
n = int(input("Enter number: "))
sum = (n*(n+1))/2
print(sum)

# Q11
a = int(input("Enter number: "))
rs = a>>2
ls= a<<2
print(rs,ls)
