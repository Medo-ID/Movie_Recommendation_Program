""" - Main app
    - App title: Find a movie to watch this night
    - User Story:
        - What type of movies you'd like to watch?
            - Enter the biginning of the genre to see if we have some recommendation: 
            -> provide the user with list of movie's genre that start with those letters if there is one.
            - Choose a genre that you like: 
            - Would you like to:
                1 - Get All the movies with this genre?
                2 - Filter Movies by release year?
                IF 1: Enter 1
                    -> provide user with list of movie (well presented data)
                ELSE: Enter 2
                    -> Choose a release year range
                    - Between this year: (first year)
                    - And this year: (second_year)
                    IF there is a result:
                        -> print it (well presented data)
                    ELSE:
                        -> "movie not found" 
"""
import csv
from movie_management_system import MovieCollection

movie_collection = MovieCollection()

with open('movies_dataset.csv') as movies_data:
    reader = csv.DictReader(movies_data)
    for row in reader:
        genre = row["Genre"]
        title = row["Title"]
        release_year = row["Release_Year"]
        rating = row["Rating"]
        movie_collection.insert_movie(genre, title, release_year, rating)

movie_dict = movie_collection.get_movies_table()

def search_for_genre_by_letters(keys, letters):
    pass

def main():
    print("""
        **************************************
        **************************************
        *                                    *
        *  Find a Movie to Watch this Night  *
        *                                    *
        **************************************
        **************************************
    """)

    print("What type of movies you'd like to watch? \n")
    user_input = input("Enter the biginning of the genre to see if we have some recommendation: ")
    