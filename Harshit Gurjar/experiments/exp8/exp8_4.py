"""4.  Input two values from user where the first line contains N, the number of test 
cases. The next N lines contain the space separated values of a and b. Perform 
integer division and print a/b. Handle exception in case of ZeroDivisionError or 
ValueError.  
Sample input 
1 0 
2 $ 
3 1  
Sample Output : 
Error Code: integer division or modulo by zero  
Error Code: invalid literal for int() with base 10: '$' 3 """


import math
N=int(input("Enter no of inputs: "))
file = open("Exp4.txt","w")
file.write(str(N))
for i in range(N):
    file.write(f"\n{input("Enter operands: ")}")
file.close()
    

file=open("Exp4.txt")
N = int(file.readline())
operands=[]

while(N>0):
    operands+=[file.readline().strip().split()]
    N-=1
for i in range(len(operands)):
    try:
        a=float(operands[i][0])
        b=float(operands[i][1])
        if ( not math.isnan(a)) and not math.isnan(b):
            quotient =a/b
            print(quotient)
        else:
            raise ValueError 
    except ZeroDivisionError as z:
        print(z)
    except ValueError as v : 
        print(v)
file.close()