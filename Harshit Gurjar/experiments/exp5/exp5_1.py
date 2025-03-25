n=input("Enter Your String: ")
l=len(n)
count=0
for i in range(l):
    if(ord(n[i])>=65 and ord(n[i])<=90):
        count=count+1

print(count)

