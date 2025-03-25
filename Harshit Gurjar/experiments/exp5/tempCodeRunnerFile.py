s1=set()
s2=set()
n1=int(input("Enter number of fruits in s1: "))
n2=int(input("Enter number of fruits in s2: "))

for i in range(n1):
    p=input("Enter fruit in s1: ")
    s1.add(p)

for i in range(n2):
    p=input("Enter fruit in s2: ")
    s2.add(p)

print(s1.intersection(s2))
print(s1.difference(s2))
print(n1+n2)
