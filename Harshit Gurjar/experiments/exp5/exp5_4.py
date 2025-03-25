n=input("Enter string: ")
m=input("Enter sub-string: ")
count=0
i=0
for i in range(i,len(n)):

    if m in n[i:i+len(m)]:
        count+=1
print(count)


