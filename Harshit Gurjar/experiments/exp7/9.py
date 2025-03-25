def palindrome(n):
     n=input("enter a number: ")
     x=int(n)
     c=x
     l=len(n)
     i=1
     while(i<=l):
        a=x%10
        b=int(c/(10**(l-i)))
        x=int(x/10)
        c=int(c%(10**(l-i)))
        if(a==b):
            number="palindrome"
            i+=1
        else:
            number="not palindrome"
            break
     print(number)

n=int(input("Enter number to check if it is palindrome: "))
palindrome(n)