n=input("Enter a number: ")
l=len(n)
n=int(n)

sum=0

for i in range(l):
    a=n%10
    sum=sum+a
    n=int(n/10)

print(sum)