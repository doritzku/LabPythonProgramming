# Experiment 6 - by Ravi Ardhana 590013582 B-10

# Q1
l=[]
for _ in range(int(input("Enter no of elements: "))):
    x = float(input())
    l.append(x)
leng=len(l)

# by sliced list
for i in range(leng):
    count=0
    if l[i] not in l[0:i]:
        for j in range(leng):
            if l[i]==l[j]:
                count+=1
        print(l[i],count)

# by extra list
counted=[]
for i in range(len(l)):
    count =0
    if l[i] not in counted: 
        for j in range(len(l)):
            if (l[i]==l[j]):
                count+=1
        counted.append(l[i])
        print(l[i],count)

# by dictionary
count_dict={}
for num in l:
    if num in count_dict:
        count_dict[num]+=1
    else:
        count_dict[num]=1
print(count_dict)
for key in count_dict:
    print(key,count_dict[key])

#Q2
l=[]
for _ in range(int(input("Enter no of elements: "))):
    x = float(input())
    l.append(x)
l =tuple(l)
sum=0
for i in range(len(l)):
    sum+=l[i]
avg=sum/len(l)
print(avg)

#Q3
a=[]
for _ in range(int(input("Enter no: "))):
    a.append(int(input()))
a.sort()
length= len(a)
for i in range(length):
    if a[length-i-1]!=a[length-i-2]:
        print(a[length-i-2])
        break
    else:
        if a[0]==a[length-i-1]:
            print(a[0])
            break

#Q4
PersonInfo={}
for _ in range(int(input("Enter no of people: "))):
    name=input("Enter name:")
    city=input("Enter City:")
    PersonInfo[name]=city
# print(PersonInfo)

nameList= list(PersonInfo.keys())
cityList= list(PersonInfo.values())
# print(nameList,cityList)

# (a) 
# for _ in range(len(nameList)):
#     print(nameList[_], end=" ")
for name in PersonInfo:
    print(name,end=" ")
print()

# (b) 
# for _ in range(len(cityList)):
#     print(cityList[_], end=" ")
for name in PersonInfo:
    print(PersonInfo[name],end=" ")
print()

#(c)
# for i in range(len(PersonInfo)):
#     print(f"{nameList[i]} from {cityList[i]}")
for name in PersonInfo:
   print(f"{name} from {PersonInfo[name]}")

#(d)
city1=[]
city2=[]
for name in PersonInfo:
    city1.append(PersonInfo[name])

for name in PersonInfo:
    count= city1.count(PersonInfo[name])
    if PersonInfo[name] not in city2:
        city2.append(PersonInfo[name])
        print(PersonInfo[name],count)

#Q5
Movies={}
info_dict={}
n=int(input("Enter no of Movies: "))
for _ in range(n):
    name=input("Enter name:")
    year=int(input("Enter year: "))
    dir_name=input("Enter directors name: ")
    cost= int(input("Enter production cost: "))
    profit= int(input("Enter profit: "))
    info_dict={
        "Title":name,
        "Year": year,
        "Directed by": dir_name,
        "Cost of Production": cost,
        "Profits Earned" : profit,
    }
    Movies[name]=info_dict

print(Movies)

for name in Movies:
    if(Movies[name]["Year"]<2015):
        print(Movies[name]["Title"])
    if(Movies[name]["Profits Earned"]>0):
        print(Movies[name]["Title"])
    if("James" ==Movies[name]["Directed by"]):
        print(Movies[name]["Title"])

    
