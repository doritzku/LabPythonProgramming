# Create a tuple to store n numeric values and find average of all values.
t="thik hai bhai"
n=int(input("Enter number of numeric values: "))
list1=[]

for i in range(n):
    y=int(input("Enter a numeric value: "))
    list1.append(y)

mytup=tuple(list1)


sum=0
for i in range(n):
    sum=sum+mytup[i]

average=sum/n
print(average)
