#2. Store integers in a file. 
#a. Find the max number 
#b. Find average of all numbers 
#c. Count number of numbers greater than 100 


f=open("num.txt","w")

f.write("1\n2\n3\n99\n4321\n234\n53242\n9")
f.close

#All numbers:
f=open("num.txt","r")
data=f.read()
print(data)
n=data.split()
#print max number:
greatest=0
for i in n:
    if int(i)>=greatest:
        greatest=int(i)
print(f"The greatest number is {greatest}")
f.close()
#Average of all numbers:
sum=0
for i in n:
    sum=sum+int(i)
average=sum/len(n)
print(average)
#numbers greater than 100:
count=0
for i in n:
    if int(i)>100:
        count+=1
print(f"Number of numbers greater than 100 is {count}")


f.close()


