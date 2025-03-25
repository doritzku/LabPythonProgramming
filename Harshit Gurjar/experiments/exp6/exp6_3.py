
n=int(input("Enter number of students: "))
mylist=[]
for i in range(n):
    s=int(input(f"Enter score of student {i+1}:"))
    mylist.append(s)
winner=0

for i in range(n):
    if winner<=mylist[i]:
        winner=mylist[i]
runner_up=0
for i in range(n):
    if mylist[i]!=winner:
        if runner_up<=mylist[i]:
            runner_up=mylist[i]
print(runner_up)



