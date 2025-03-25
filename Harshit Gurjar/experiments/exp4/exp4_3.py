n=int(input("Enter a number: "))
i=0
p=0
q=1
while(i<n):

    r=p+q
    print(p, end=("  "))
    p=q
    q=r
    i+=1