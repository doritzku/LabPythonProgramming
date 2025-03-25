n=input("Enter your string:")
n=n.upper()
alphabets=[]

for i in range(len(n)):

    if n[i] not in alphabets:
        if (n[i]!=" "):    
            alphabets.append(n[i])
            print(n.count(n[i]),n[i])



"""    count=0
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i]!= " ":
                if(n[i]==n[j]):
                    count=count+1
                
        print(count,n[i])
        count=0
    """