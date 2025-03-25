n=int(input("Enter a number"))
if(n<=0):
    print("Enter a positive number: ")
else:
    i=1
    fact=1
    while(i<=n):
        fact=i*fact
        i+=1
    print(f"Factorial is {fact}")
