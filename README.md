# Movie Management System

## Overview

This project is a movie management system that allows users to search for movies by genre and filter them by release year. The system is composed of three main files:

1. `app.py`: The main application file that provides the user interface and handles user interactions.
2. `movie_management_system.py`: The module defining the data structures and methods for managing a collection of movies.
3. `movies_dataset.csv`: A CSV file containing the movie data.

## Files

### app.py

This is the main application file. It loads the movie data from the CSV file into a `MovieCollection` object and provides an interactive command-line interface for users to find movies.

#### Functions

- **`search_for_genre_by_letters(letters)`**:
  Searches for genres that start with the given letters.

  - **Parameters**:
    - `letters (str)`: The starting letters of the genre to search for.
  - **Returns**:
    - `list`: A list of genres that match the given starting letters.

- **`main()`**:
  The main function that provides an interactive interface for users to search for and filter movies.
  - **Description**:
    - Displays a welcome message and prompts the user to enter the beginning of a genre to see if there are any recommendations.
    - Allows the user to choose a genre and decide whether to get all movies of that genre or filter them by release year.
    - If the user chooses to filter by release year, prompts the user to enter a range of years and displays the movies within that range.
    - The user can exit the program at any point by entering 'n'.

### movie_management_system.py

This module defines the data structures and methods for managing a collection of movies categorized by genre. It provides functionalities to insert movies, retrieve movies by genre, and search for movies within a specific release year range.

#### Classes

- **`MovieNode`**: Represents a node in the movie linked list.

  - **Attributes**:
    - `title (str)`: The title of the movie.
    - `release_year (int)`: The release year of the movie.
    - `rating (str)`: The rating of the movie.
    - `next_movie_node (MovieNode)`: The next node in the linked list.

- **`MovieLinkedList`**: A linked list to manage movies.

  - **Methods**:
    - `insert_beginning(title, release_year, rating)`: Inserts a new movie node at the beginning of the list.
    - `get_data()`: Returns a formatted string of all movies in the list.
    - `get_data_by_release_year(start_year, end_year)`: Returns a list of movies released within the specified year range.

- **`MovieCollection`**: A collection of movies categorized by genre.
  - **Attributes**:
    - `genre_table (dict)`: A dictionary mapping genres to `MovieLinkedList` objects.
  - **Methods**:
    - `get_movies_table()`: Returns the dictionary of genres and their corresponding movie linked lists.
    - `insert_movie(genre, title, release_year, rating)`: Inserts a movie into the collection under the specified genre.
    - `get_movies_by_genre(genre)`: Returns a formatted string of all movies in the specified genre.
    - `search_movies_by_year_range(start_year, end_year)`: Searches for movies across all genres within the specified year range.

### movies_dataset.csv

This file contains the movie data used by the system. It includes the following columns:

- `Genre`: The genre of the movie.
- `Title`: The title of the movie.
- `Release_Year`: The release year of the movie.
- `Rating`: The rating of the movie.

## Usage

1. Ensure all files (`app.py`, `movie_management_system.py`, and `movies_dataset.csv`) are in the same directory.
2. Run the `app.py` script.
3. Follow the on-screen prompts to search for movies by genre or filter them by release year.

```bash
python app.py

**************************************
**************************************
*                                    *
*  Find a Movie to Watch this Night  *
*                                    *
**************************************
**************************************

What type of movies you'd like to watch?

Enter the beginning of the genre to see if we have some recommendations: Act
Genres with these letters are: ['Action']
Choose a genre that you like. / Enter n to reset the app: Action
Would you like to:
1 - Get All the movies with this genre?
2 - Filter Movies by release year?
n - To exit the app?
1
========================================================
Title: Die Hard
Release Date: 1988
Rating: 8.2
========================================================
Title: Mad Max: Fury Road
Release Date: 2015
Rating: 8.1
...
```
