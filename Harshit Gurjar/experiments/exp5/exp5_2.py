"""n=(input("Enter a string: "))
count=0

for i in range(len(n)):
     if(n[i]=="a" or n[i]=="e" or n[i]=="i" or n[i]=="o" or n[i]=="u"):
      count=count+1
print(count)
"""
        

n=input("Enter your string: ")
count=0
for i in range(len(n)):
    if n[i].lower() in "aeiou":
        count+=1
print(count)