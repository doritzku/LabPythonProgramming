n=int(input("Enter number of movies: "))
mydict={}

for i in range(n):
    movie=input("Enter movie name: ")
    director=input("Enter director: ")
    prod_cost=int(input("Enter production cost: "))
    collection=int(input("Enter total collection: "))
    Year=int(input("Enter year of release: "))
    mydict[movie]={"director":director,
                   "production cost":prod_cost,
                   "collection":collection,
                   "Year":Year}
                   
#print all movie details
print("movie details: ")
for movie in mydict:
    print((f"{movie}:"))
    print("director:",mydict[movie]["director"])
    print("Year of release: ",mydict[movie]["Year"])
    print("Total collection: ",mydict[movie]["collection"])
    print("Total production cost: ",mydict[movie]["production cost"])
    


#display name of movies released before 2015 
print("\nMovies before 2015 are:\n ")
for movie in mydict:
    if mydict[movie]["Year"]<2015:
        print(movie)

#movies that made profit
print("Movies that made profit are: ")
for movie in mydict:
    if mydict[movie]["collection"]>mydict[movie]["production cost"]:
        print(movie)


#Movies directed by a director:
a=[]
for movie in mydict:
    b=movie
    if mydict[movie]["director"] not in a:
        a.append(mydict[movie]["director"])
        print(f"Movies directed by {mydict[movie]["director"]}: ")

        for movie in mydict:
            if mydict[movie]["director"]==mydict[b]["director"]:
                print(movie)