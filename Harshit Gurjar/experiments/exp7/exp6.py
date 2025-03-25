n=int(input("Enter number of movies: "))
mylist=[]
movies_before_2015=[]
profit=[]
directors=[]
movies_of_dir=[]
mydict={}
for i in range(n):
    name=input("Enter name of movie:")
    year=int(input("Enter year released:  "))
    # dir_name=input("Enter director name: ")
    # prod_cost=int(input("Enter production cost(in CR): "))
    # collection=int(input("Enter collection made(in CR): "))
    mydict[name]= { "name": name,
            "year":year,
            # "director name":dir_name,
            # "production cost":prod_cost,
            # "collection":collection,
            }

#a) Print alll movie details
print(mydict)
for name in mydict:
    for info in mydict[name]:
        print(mydict[name][info])

# for movie,details in mydict.keys():
#      print(f"{details.capitalize()}:{details}")


## ZIP Function
# tup = (1,2,3,4)
# lis= [9,8,7,6,5]
# a=set()
# print(type(a))
