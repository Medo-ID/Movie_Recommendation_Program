import sys
import csv
from movie_management_system import MovieCollection

# Initialize the movie collection
movie_collection = MovieCollection()

# Load movies from the CSV file into the movie collection
with open('movies_dataset.csv') as movies_data:
    reader = csv.DictReader(movies_data)
    for row in reader:
        genre = row["Genre"]
        title = row["Title"]
        release_year = row["Release_Year"]
        rating = row["Rating"]
        movie_collection.insert_movie(genre, title, release_year, rating)

# Dictionary to hold movies by genre
movies_dict = movie_collection.get_movies_table()

def search_for_genre_by_letters(letters):
    """
    Searches for genres that start with the given letters.
    
    Parameters:
    letters (str): The starting letters of the genre to search for.
    
    Returns:
    list: A list of genres that match the given starting letters.
    """
    result = []
    for genre in movies_dict:
        if genre.lower().startswith(letters.lower()):
            result.append(genre)
    return result

def main():
    """
    Main function to interact with the user. Allows users to search for movies by genre and filter movies by release year.
    """
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
    user_input = input("Enter the beginning of the genre to see if we have some recommendations: ")
    genres = search_for_genre_by_letters(user_input)
    
    while not user_input or not genres:
        user_input = input("No genres with these letters! Try Again: ")
        genres = search_for_genre_by_letters(user_input)
    
    print(f"Genres with these letters are: {genres}")
    user_choice = input("Choose a genre that you like. / Enter n to reset the app: ")
    
    while not user_choice or user_choice.capitalize() not in movies_dict:
        if user_choice.lower() == 'n':
            main()
            return
        print(f"Genres with these letters are: {genres}")
        user_choice = input("Choose a genre that you like. Make sure you enter one of the above genres. / Enter n to reset the app: ")

    user_decision = input("""Would you like to:
1 - Get All the movies with this genre?
2 - Filter Movies by release year?
n - To exit the app?
""")
    
    while user_decision != '1' and user_decision != '2' and user_decision.lower() != 'n':
        user_decision = input("""Make sure you enter the right answer. Would you like to:
1 - Get All the movies with this genre?
2 - Filter Movies by release year?
n - To exit the app?
""")

    if user_decision.lower() == 'n':
        sys.exit()

    if user_decision == '1':
        movies = movie_collection.get_movies_by_genre(user_choice.capitalize())
        if movies:
            print(movies)
        else:
            print("No movies yet for this genre.")
        
    if user_decision == '2':
        print("""To start your search, we need you to select a search range of two specific years to search for movies between them. 
Note: The first year must be less than or equal to the second year.
""")
        start_year = input("Between: ")
        end_year = input("And: ")
        
        while not (start_year.isdigit() and end_year.isdigit() and int(start_year) <= int(end_year)):
            print("Make sure you follow the rules")
            start_year = input("Between: ")
            end_year = input("And: ")

        movies = movies_dict[user_choice.capitalize()].get_data_by_release_year(start_year, end_year)
        
        if movies:
            for movie in movies:
                print("========================================================\n"
                    + f"Title: {movie.title}\n"
                    + f"Release Date: {movie.release_year}\n"
                    + f"Rating: {movie.rating}\n"
                )
        else:
            print("No movies found between these two years.")
            last_decision = input("Enter y to start again. n to exit the program: ")
            while last_decision != 'y' and last_decision != 'n':
                last_decision = input("Please, Enter y to start again. n to exit the program: ")
            if last_decision.lower() == 'y':
                main()
            if last_decision.lower() == 'n':
                sys.exit()

# Start the main program
main()
