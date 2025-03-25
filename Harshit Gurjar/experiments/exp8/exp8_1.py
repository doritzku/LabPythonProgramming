
"""with open("name.txt", "w") as file:
    file.write("cbum\ntusR\nreV\nhrsh\nVirat\nRohitS\nArds")


with open("name.txt", "r") as file:
    names = [line.strip() for line in file.readlines()]


total_names = len(names)

vowels = {'A', 'E', 'I', 'O', 'U'}
vowel_names = [name for name in names if name[0].upper() in vowels]
vowel_count = len(vowel_names)

longest_name=""
for name in names:
    if len(longest_name)<=len(name):
        longest_name=name

print(f"Total number of names: {total_names}")
print(f"Number of names starting with a vowel: {vowel_count}")
print(f"Longest name: {longest_name}")
"""



f=open("file.txt","w")
f.write("Harshit\nRavi\nShivam\nNames\nUnion\nArd\nAngry\nYamrajDevta")
f.close()
f=open("file.txt","r")
data=f.read()
print(data)
#no. of names
n=data.split()
print(len(n))
#no. of names starting with vowel
vowels=("A","E","I","O","U")
count=0
for names in n:
    if names[0] in vowels:
        count+=1
        
print(count)
#To print longest name:
longest=""
for names in n:
    if len(names)>len(longest):
        longest=names

print(f"the longest name is {longest}")
f.close()
