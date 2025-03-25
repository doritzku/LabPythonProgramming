n=input("Enter a sentence: ")
words=n.split()

myset=set()
for i in range(len(words)):
    myset.add(words[i])


print(len(myset))
