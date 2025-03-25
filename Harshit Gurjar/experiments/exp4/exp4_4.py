n=int(input("Enter a number: "))
i=2
if(n<=0):
      number="Not positive"
else:
    if(n==1 or n==2):
            number="prime"

    else:

        while(i<n):
                    
            if((n%i)!=0):
                    i+=1
                    number="prime"
            else:
                    number="not prime"
                    break
print(f"Number is {number}")