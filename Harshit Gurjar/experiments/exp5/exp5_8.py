
s1={"Red","yellow","orange","blue"}
s2={"violet","blue","purple"}


print(s1.intersection(s2))
print(s2.union(s1))
print(s1.difference(s2))


s1.pop()
s1.pop()
s2.pop()

print(s1)
print(s2)
