# # Write your solution here

# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), 
# which adds a new movie object into a movie database.

# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

#     name
#     director
#     year
#     runtime

# The values attached to these keys are given as arguments to the function.




def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie = {}
    movie["name"] = name
    movie["director"] = director
    movie["year"] = year
    movie["runtime"] = runtime
    database.append(movie)
    
        # movie = {"name": name,

        #        "director": director,

        #        "year": year,

        #        "runtime": runtime}
    
    
    









if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)