def createList(*n):
    mylist=[]
    for i in range(len(n)):
        mylist.append(n[i])

    return mylist
    

a=createList(3,2,4,5)
print(a)