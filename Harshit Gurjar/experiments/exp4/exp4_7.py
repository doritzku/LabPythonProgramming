#Count and print all numbers divisible by 5 or 7 between 1 to 100
count=0
i=5
while(i<=100):
    if(i%5==0 or i%7==0):
        print(i)
        count+=1
    i+=1
print("The total count is", count)



#Count and print all numbers divisible by 5 or 7 between 1 to 100
count1=0
count2=0
i=5
while(i<=100):
    if(i%5==0):
        print(i,"is divisible by 5")
        count1+=1
    
    if(i%7==0):
        print(i,"is divisible by 7")
        count2+=1
    
    i+=1

print("The total count of divisible by 5 is is", count1)
print("The total count of divisible by 7 is is", count2)
