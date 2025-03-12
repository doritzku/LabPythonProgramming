# Experiment 7 - by Ravi Ardhana 590013582 B-10

#LAB Questions
# Q1 Required argument
def Even_Odd(n):
    n=10
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
    
Even_Odd(2)

# Q2 keyword argument
def printInfo(name,address):
    print(name,address)
printInfo(address='UPES',name="Ravi")

# Q3 Default Argument
def greet(name,n="Good Morning"):
    print(n,name)
greet("Ravi")

# Q4 Variable length Argument
def printNames(*names):
    for i in range(len(names)):
        print(names[i])
printNames("A","B","C")

# Q5 Armstrong No
def IsArmstrong(n):
    length = len(str(n))
    sumOfCube= 0
    x=n
    for i in range(length):
        digit= x%10
        x = x//10
        sumOfCube+=(digit)**length
    if (sumOfCube==n):
        print("Is Armstrong no.")
    else:
        print("Is not Armstrong no!")

IsArmstrong(153)

# Q6 Factorial
def Factorial(n):
    i=n
    fact=1
    while(i>0):
        fact*=i
        i-=1
    print(fact)
Factorial(5)

# Q7 Fibonacci
def n_Fibonacci_terms(n):
    i=0
    a=0
    b=1
    c=0
    while(i<n):
        c=a+b
        print(a)
        a,b=b,c
        i+=1
n_Fibonacci_terms(3)

# Q8 Prime number
def IsPrime(n):
    if (n==1 or n==0):
        return print(n,"Enter valid integer")
    for i in range(2,n):
        if(n%i==0):
            return print(n,"is not prime.")
    return print(n,"is prime")
IsPrime(97)

# Q9 Palindrome
def IsPalindrome(n):
    x= int(n)
    c=x
    length = len(str(n))
    i=1
    while(i<=length):
        a = x%10
        b = int(c/(10**(length-i)))
        x= int(x/10)
        c = int(c%(10**(length-i)))
        if(a==b):
            number = "is palindrome"
            i+=1
        else:
            number = "is not palindrome"
            break
    print(n,number)

IsPalindrome("1231")

# #Q10 Lamda Function
def Even_Odd1(n):
    if(n%2==0):
        return 1
    else:
        return 0
Even_Odd2= lambda x: 1 if x%2==0 else 0
print(Even_Odd1(5))
print(Even_Odd2(5))

##########################Experiment -7########################

# #Q1
def Max(*numbers):
    max=numbers[0]
    for i in numbers:
        if max<i:
            max=i
    return max

n=Max(2,3,4,5,6,7,8,8,4,3,3,68)
print(n)

def Min(*numbers):
    min=numbers[0]
    for i in numbers:
        if min>i:
            min=i
    return min
n=Min(-2,3,4,5,6,7,8,8,4,3,3,68)
print(n)

# #Q2 // Returns sum of cubes smaller than the argument number 
def sumOfCubes(n):
    sum=0
    for i in range(1,n):
        sum+=(i**3)
    return sum
print(sumOfCubes(3))

#Q3 // print number 1 to n
def print_till_n(n):
    if(n>0):
        print(n)
        print_till_n(n-1)
print_till_n(10)

# #Q4 // print fibonacci upto n
def n_fibonacci(n,x=0,y=1):
    if n>0:
        print(x,end=" ")
        n_fibonacci(n-1,y,x+y)
n_fibonacci(8)

# #Q5 // volume of cone using lambda function
from math import pi
# pi=22/7
Volume_of_Cone= lambda r,h: (pi*(r**2)*h)/3
print(Volume_of_Cone(7,7))

#Q6 // volume of cone using lambda function
l=[1,2,3,45,232,-1]
Min_Max= lambda l:(max(l),min(l))
print(Min_Max(l))

#Q7
def nth_fibonacci(n):
    if n==1 or n==0:
        return 0
    if n==2:
        return 1
    return nth_fibonacci(n-1)+nth_fibonacci(n-2)
print("\n{}".format(nth_fibonacci(8)))




