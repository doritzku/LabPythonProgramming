# Experiment 5 - by Ravi Ardhana 590013582 B-10

#Q1
n= input("Enter a string: ")
print("By ASCII values: ")
for i in range(len(n)):
    if(ord(n[i]) in range(65,91)):
        print("Yes",n[i],(ord(n[i])))
    
print("By isupper function: ")
for i in range(len(n)):
    if n[i].isupper():
        print("Yes",n[i],(ord(n[i])))
    
#Q2
n= input("Enter a string: ")
vowelCount=0
for i in range(len(n)):
    if(n[i]=='a'or n[i]=='A' ):
        vowelCount+=1
    if(n[i]=='e'or n[i]=='E' ):
        vowelCount+=1
    if(n[i]=='i'or n[i]=='I' ):
        vowelCount+=1
    if(n[i]=='o'or n[i]=='O' ):
        vowelCount+=1
    if(n[i]=='u'or n[i]=='U' ):
        vowelCount+=1
print(vowelCount)


#Q3
n= input("Enter a string: ")

for i in range(len(n)):
    if(n[i]!=" "):
        print(n[i],end="")
    else:
        print("\n",end="")
    
#Q4
String= input("Enter a string: ")
subString= input("Enter sub-string: ")
slen =len(String)
subSlen =len(subString)
count=0
for i in range(slen):
    if (subString==String[i:subSlen+i]):
        count +=1
print(count)

#Q5
String= input("Enter a string: ")
count =0
for i in range(65,91):
    if(chr(i) in String or chr(32+i) in String):
        for j in range(len(String)):
            if (ord(String[j])==i or ord(String[j])==(i+32) ):
                count +=1
            
        print(chr(i),count)
    count=0

# Q6
sentence = input("Enter Sentence: ")
uniqueWords= set({})
Blank=0
nextBlank=0
print(len(sentence))
for i in range(len(sentence)):
    if(sentence[i]==" " or i==(len(sentence)-1) ):
        if (i==(len(sentence)-1)):
            nextBlank=i+1
        else:
            nextBlank=i
        uniqueWords.add(sentence[Blank:nextBlank].strip())
        Blank= nextBlank
print(uniqueWords)


#Q7
s1 = {"Apple","Banana","Cherimoya"}
s2 = {"DragonFruit","Emblica","Fig","Cherimoya"}
commonFruit= s1.intersection(s2)
fruitsOnlyInSet1= (s1-s2)
totalFruits= (len(s1.union(s2)))
print(s1)
print(s2)
print(commonFruit)
print(fruitsOnlyInSet1)
print(totalFruits)

#Q8
s1= {"Red","Yellow","Orange","Blue"}
s2= {"Violet","Blue","Purple"}
print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Subtract:",(s1-s2))
