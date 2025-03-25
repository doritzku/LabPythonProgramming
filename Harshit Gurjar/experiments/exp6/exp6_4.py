""" Create a dictionary of n persons where key is name and value is city.  
a) Display all names 
b) Display all city names 
c) Display student name and city of all students. 
d) Count number of students in each city."""

mydict={}
n=int(input("Enter number of people: "))
for i in range(n):
    p=input(f"Enter name of person{i+1}:")
    mydict[p]=input("which city is he from: ")
#1
for keys in mydict:
    print(keys)
#2
for keys in mydict:
    print(mydict[keys])
#3
for keys in mydict:
    print(f"{keys}:{mydict[keys]}")
#4
mylist=[]
mylist2=[]
for key in mydict:
    mylist.append(mydict[key])

for key in mydict:
    if mydict[key] not in mylist2:
        mylist2.append(mydict[key])
        print(mydict[key],mylist.count(mydict[key]))
