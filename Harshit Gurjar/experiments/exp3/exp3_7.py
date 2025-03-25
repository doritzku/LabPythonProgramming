day=int(input("Enter day: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))

if(month==2):
    if(day>28):
        print("Enter a valid date: ")
else:
        if(month==2):
            if(day==28):
                day=1
                month=month+1
            else: 
                day=day+1
        else:
            if(day<31):            
                day=day+1
            elif(day==31):
                if(month<12):
                    month= month+1
                elif(month==12):
                    day=1
                    month=1
                    year=year+1
        print(f"The next date will be {day}/{month}/{year}")
        


