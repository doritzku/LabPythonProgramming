# Experiment 4 - by Ravi Ardhana 590013582 B-10

# Q1 - Factorial
n = int(input("Enter number: "))
i=n
fact=1
while(i>0):
    fact*=i
    i-=1
print(fact)

# Q2 - Armstrong number
n = int(input("Enter number: "))
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

#Q3 - Fibonacci series
n = int(input("Enter the term: "))
i=0
a=0
b=1
c=0
for i in range(n):
    print(a)
    c=a+b
    a,b=b,c
while(i<n):
    c=a+b
    print(a)
    a,b=b,c
    i+=1

# Q4 -Is prime
n = int(input("Enter a natural number: "))
isPrime = True
i=2
if(n==1 or n==0):
        print("Enter valid integer")    
else:
    while(i<n):
        if(n%i==0):
            print("NOt prime.")
            isPrime = False
            break
        i+=1
    # for i in range(2,n):
    #     if(n%i==0):
    #         print("NOt prime.")
    #         isPrime = False
    #         break
    if (isPrime):
        print("Is prime")   
    
# Q5
n = (input("Enter a natural number: "))
x= int(n)
c=x
length = len(n)
i=1
while(i<=length):
    a = x%10
    b = int(c/(10**(length-i)))
    x= int(x/10)
    c = int(c%(10**(length-i)))
    if(a==b):
        number = "palindrome"
        i+=1
    else:
        number = "not palindrome"
        break
print(number)


# Q6
n = int(input("Enter a natural number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
sum= ((n+1)*n)/2
print(sum)

# Q7 
count = 0
for i in range(1,101):
    if(i%5==0 or i%7==0):
        print(i)
        count+=1
print("Count= ",count)

# Q8
str = input("Enter string: ")
new_str = str.upper()
print(new_str)

# Q9
n=1
while(n<100):
    isPrime = True
    i=2
    while(i<n):
            if(n%i==0):
                isPrime = False
                break
            i+=1
    if (isPrime):
        print(n)   
    n+=1

# Q10
n = int( input("Enter number: "))
i=1
while(i<11):
    print(n,"*",i,"=",n*i)
    i+=1

