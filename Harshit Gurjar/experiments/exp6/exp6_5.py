
# Taking input for number of movies
n = int(input("Enter the number of movies: "))

# Dictionary to store movie details
movie_dict = {}

# Collect movie details
for i in range(n):
    movie_name = input(f"Enter the name of movie {i + 1}: ")
    year = int(input(f"Enter the year of release for {movie_name}: "))
    director = input(f"Enter the director's name for {movie_name}: ")
    production_cost = float(input(f"Enter the production cost of {movie_name}: "))
    collection = float(input(f"Enter the earnings/collection of {movie_name}: "))
    
    # Store all movie details in the dictionary
    movie_dict[movie_name] = {
        'year': year,
        'director': director,
        'production_cost': production_cost,
        'collection': collection
    }

# a) Print all movie details
print("\nMovie Details:")
for movie, details in movie_dict.items():
    print(f"Movie: {movie}")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")
    print()

# b) Display movies released before 2015
print("\nMovies released before 2015:")
for movie, details in movie_dict.items():
    if details['year'] < 2015:
        print(movie)

# c) Print movies that made a profit
print("\nMovies that made a profit:")
for movie, details in movie_dict.items():
    if details['collection'] > details['production_cost']:
        print(movie)

# d) Print movies directed by a particular director
director_name = input("\nEnter a director's name to search their movies: ")
print(f"\nMovies directed by {director_name}:")
for movie, details in movie_dict.items():
    if details['director'].lower() == director_name.lower():
        print(movie)
