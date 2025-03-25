PDS = float(input("Enter PDS Marks: "))
Python = float(input("Enter Python Marks: "))
Chemistry = float(input("Enter Chemistry Marks: "))
English = float(input("Enter English Marks: "))
Physics = float(input("Enter Physics Marks: "))
percentage = ((English+Python+Chemistry+PDS+Physics)/500)*100 
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

print("Name: Harshit Gurjar")
print("Roll Number:R12345", end="\t\t\t") 
print("SAPID: 590012270")
print("Semester: 1", end="\t\t\t")
print("Course: B.Tech. CSE AI&ML")
print("Subject Name : Marks")
print("PDS: ", PDS)
print("Python: ", Python)
print("Chemistry: ",Chemistry)
print("English: ", English)
print("Physics: ", Physics)
print("Percentage: ",percentage,"%")
print("CGPA: ",CGPA)
print("Grade: ",Grade)
