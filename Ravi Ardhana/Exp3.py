# Experiment 3 - by Ravi Ardhana 590013582 B-10
sensordata = 60
if (sensordata>0 and sensordata<=25):
    print("25")
elif(sensordata>25 and sensordata<=50):
    print(50)
elif(sensordata>50 and sensordata<=75):
    print(75)
elif(sensordata>75 and sensordata<=100):
    print(100)

# Q1
number = 78
if(number%3==0 and number%5==0):
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")

# Q2 
number = 78
if (number%5==0):
    print("Number is not a multiple of 5")

# Q3
a= 3
b=2
if(a==b):
    print("Both are equal")
elif(a<b):
    print("a is less than b")
elif(a>b):
    print("a is greater than b")

# Q4
a= 3
b=2
if(a<b):
     print("a is less than b")
else:
    print("a is greater than b")

# Q5

# With function
def QuadraticRoots(a,b,c):
    discriminant = ((b**2)-4*a*c)
    if (discriminant>=0):
        root1 = ((-b) + (discriminant)**(1/2))/(2*a)
        root2 = ((-b) - (discriminant)**(1/2))/(2*a)
    else:
        return
    return root1, root2
a = float (input("Enter coefficient of x^2: "))
b = float (input("Enter coefficient of x: "))
c = float (input("Enter constant: "))
roots = QuadraticRoots(a,b,c)
if (roots!=None):
    print("Roots are real:",roots)
else:
    print("Roots are imaginary")

## Without function
a = float (input("Enter coefficient of x^2: "))
b = float (input("Enter coefficient of x: "))
c = float (input("Enter constant: "))
discriminant = ((b**2)-4*a*c)
if (discriminant>=0):
    root1 = ((-b) + (discriminant)**(1/2))/(2*a)
    root2 = ((-b) - (discriminant)**(1/2))/(2*a)
    print("Roots are real: ",root1, root2)
else:
    imagRoot1 = ((-discriminant)**(1/2))/(2*a)
    imagRoot2 = ((-discriminant)**(1/2))/(2*a)
    realRoot1 = ((-b)**(1/2))/(2*a)
    realRoot2 = ((-b)**(1/2))/(2*a)
    root1=f"{realRoot1}+i{imagRoot1}"
    root2=f"{realRoot2},i{imagRoot2}"
    print("Roots are imaginary.",root1,root2)


# Q6
year = int(input("Enter year: "))
c1 = year%4==0 and year%100!=0
c2 = year%400==0
# print(c1,c2)
if((c1) or (c2)):
    print("Leap year")
else:
    print("Non-Leap year")

# Q7
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
if (day==30):
    day= 1
    if(month==12):
        month=1
        year+=1
    else:
        month+=1
    
else:
    day+=1
print(day,month,year)

# Q8
PDS = float(input("Enter PDS Marks: "))
Python = float(input("Enter Python Marks: "))
Chem = float(input("Enter Chemistry Marks: "))
Eng = float(input("Enter English Marks: "))
Phy = float(input("Enter Physics Marks: "))
percentage = ((Eng+Python+Chem+PDS+Phy)/500)*100 
CGPA = percentage/10
if (CGPA>0 and CGPA<=3.4):
    Grade = "F"
elif (CGPA>3.4 and CGPA<=5.0):
    Grade = "C+"
elif (CGPA>5.0 and CGPA<=6.0):
    Grade = "B"
elif (CGPA>6.0 and CGPA<=7.0):
    Grade = "B+"
elif (CGPA>7.0 and CGPA<=8.0):
    Grade = "A"
elif (CGPA>8.0 and CGPA<=9.0):
    Grade = "A+"
elif (CGPA>9 and CGPA<=10.0):
    Grade = "O"

print("Name: Ravi Ardhana")
print("Roll Number:R1738912", end="\t\t\t") 
print("SAPID: 590013582")
print("Semester: 1", end="\t\t\t")
print("Course: B.Tech. CSE AI&ML")
print("Subject Name : Marks")
print("PDS: ", PDS)
print("Python: ", Python)
print("Chemistry: ",Chem)
print("English: ", Eng)
print("Physics: ", Phy)
print("Percentage: ",percentage,"%")
print("CGPA: ",CGPA)
print("Grade: ",Grade)