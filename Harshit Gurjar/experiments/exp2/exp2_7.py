x=int(input("Enter time in seconds: "))
hours=int(x/3600) # x/3600 gives the hours
minutes=int((x%3600)/60) # x%3600 gives the remaining seconds after converting to hours
print(f"The time in minutes is {hours}:{minutes}:{x%60}") 