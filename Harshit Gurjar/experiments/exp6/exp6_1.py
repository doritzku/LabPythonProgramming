#1. Scan n values in range 0-3 and print the number of times each value has occured.
k=int(input("Enter the number of values: "))
a=[]
b=[]

for i in range(k):
    n=input("Enter a number between 0-3: ")
    a.append(n)

for i in range(k):
    if(a[i] not in b):
        b.append(a[i])
        print(a.count(a[i]),a[i])