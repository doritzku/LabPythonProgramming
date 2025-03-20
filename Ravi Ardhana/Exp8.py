# Experiment 8 - by Ravi Ardhana 590013582 B-10

## Q1.
file = open("name.txt",'w')
names=["Ravi","Shivam","Harshit","Tushar","Ardhana","Elephant","Ichimaru","Orichimaru"]
for i in range(len(names)):
    file.write(names[i]+"\n")
file.close()

# #(a)
file = open("name.txt")
name = file.read().strip()
li= name.split("\n")
print(li,f"\nTotal no. of names: {len(li)}")
file.close()

# # (b)
file = open("name.txt")
vowels=["A","E","I","O","U"]
for line in file:
    if line[0] in vowels:
        print(line.strip())
file.close()

# # (c)
file = open("name.txt")
max=-1
name= file.readlines()
for i in range(len(name)-1):
    if(len(name[i+1])>len(name[i])):
        max=name[i+1]
    else:
        max=name[i]
print(max.strip())
file.close()

## Q2.
import random
file = open("numbers.txt",'w')
Numbers=[]
for _ in range(7):
    Numbers.append(random.randint(-500,500))
for i in range(len(Numbers)):
    file.write(f"{Numbers[i]} ")
file.close()

# (a)
file = open("numbers.txt")
data = file.read().strip().split(" ")
max = int(data[0])
for i in range(1,len(data)):
    if int(data[i])>max:
        max= int(data[i])
print(data)
print(max,type(max))
file.close()
# (b)
file = open("numbers.txt")
data = file.read().strip().split(" ")
sum=0
gt100= []
for i  in range(len(data)):
    if(int(data[i])>100):
        gt100.append(int(data[i]))
    sum+=int(data[i])
avg = sum/len(data)
print(data)
print(avg)

# (c)
print(gt100)
file.close()

## Q3
file = open("city.txt")
cityinfo= {}
for line in file:
    info= line.strip().split(" ")
    cityinfo[info[0]]={"Population":info[1],"Area":info[2]}

#(a)
for key in cityinfo:
    print(key, cityinfo[key]["Population"],cityinfo[key]["Area"])

#(b)
for key in cityinfo:
    if float(cityinfo[key]["Population"])>10:
        print(key,cityinfo[key]["Population"])

#(c)
sum=0
for key in cityinfo:
    sum+=float(cityinfo[key]["Area"])
print(sum)
file.close()

##Q4
import math
N=int(input("Enter no of inputs: "))
file = open("Exp4.txt","w")
file.write(str(N))
for i in range(N):
    file.write(f"\n{input("Enter operands: ")}")
file.close()
    

file=open("Exp4.txt")
N = int(file.readline())
operands=[]

while(N>0):
    operands+=[file.readline().strip().split()]
    N-=1
for i in range(len(operands)):
    try:
        a=float(operands[i][0])
        b=float(operands[i][1])
        if ( not math.isnan(a)) and not math.isnan(b):
            quotient =a/b
            print(quotient)
        else:
            raise ValueError 
    except ZeroDivisionError as z:
        print(z)
    except ValueError as v : 
        print(v)
file.close()