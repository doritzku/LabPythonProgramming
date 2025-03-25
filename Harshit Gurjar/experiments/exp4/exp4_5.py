n=input("enter a number: ")
l=len(n)
n=int(n)

c=n

i=1
while(i<=l):
    a=n%10
    b=int(c/(10**(l-i)))
    n=int(n/10)
    c=int(c%(10**(l-i)))
    if(a==b):
        number="palindrome"
        i+=1
    else:
        number="not palindrome"
        break
print(number)