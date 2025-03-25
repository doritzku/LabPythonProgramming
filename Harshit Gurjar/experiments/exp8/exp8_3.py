"""3. Assume a file city.txt with details of 5 cities in given format (cityname 
population(in lakhs) area(in sq KM) ): 
Example: 
Dehradun 5.78 308.20 
Delhi 190 1484 
…………… 
Open file city.txt and read to: 
a. Display details of all cities 
b. Display city names with population more than 10Lakhs 
c. Display sum of areas of all cities """
file=open("city.txt","w")
file.write("Dehradun 5.78 155\nDelhi 105 1024\nMumbai 9999 175\nKolkata 123 999\nChennai 4.75 1232")
file = open("city.txt")
cityinfo= {}
for line in file:
    info= line.strip().split(" ")
    cityinfo[info[0]]={"Population":info[1],"Area":info[2]}

#Details of all cities
for key in cityinfo:
    print(key, cityinfo[key]["Population"],cityinfo[key]["Area"])

#Names with population more than 10 lakhs
for key in cityinfo:
    if float(cityinfo[key]["Population"])>10:
        print(key,cityinfo[key]["Population"])

#total area of all cities
sum=0
for key in cityinfo:
    sum+=float(cityinfo[key]["Area"])
print(sum)
file.close()
