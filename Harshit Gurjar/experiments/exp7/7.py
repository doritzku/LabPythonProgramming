def getNextdate(day,month,year):
     
     if(day<31):
        day=day+1
     elif(day==31):
        day=1
        if(month<12):
            month= month+1
        elif(month==12):
            month=1
            year=year+1

     print(f"The next date will be {day}/{month}/{year}")

day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
getNextdate(day,month,year)