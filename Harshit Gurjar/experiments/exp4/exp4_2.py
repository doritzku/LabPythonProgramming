n=input("Enter a number: ")
b=int(n)
l=len(n)
i=0
sum_of_cubes=0
while(i<l):
    a=b%10
    b=int(b/10)
    sum_of_cubes= a**3 + sum_of_cubes
    i+=1
    
if(sum_of_cubes==int(n)):
    print("The number is an Armstrong number")
else:
    print("Not an Armstrong number")