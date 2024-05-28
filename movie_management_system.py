""" 
Movie Management System 

This module defines the data structures and methods for managing a collection of movies 
categorized by genre. It provides functionalities to insert movies, retrieve movies by 
genre, and search for movies within a specific release year range.
"""
class MovieNode:
    def __init__(self, title, release_year, rating, next_movie_node=None):
        self.title = title
        self.release_year = int(release_year)
        self.rating = rating
        self.next_movie_node = next_movie_node
    
    def __repr__(self):
        return f"MovieNode({self.title}, {self.release_year}, {self.rating})"
    
    def set_next_movie_node(self, next_node):
        self.next_movie_node = next_node

class MovieLinkedList:
    def __init__(self):
        self.head_node = None
    
    def insert_beginning(self, title, release_year, rating):
        new_movie_node = MovieNode(title, release_year, rating)
        new_movie_node.set_next_movie_node(self.head_node)
        self.head_node = new_movie_node
    
    def get_data(self):
        well_presented_data = ""
        current_node = self.head_node
        while current_node:
            if current_node.title is not None:
                well_presented_data += (
                    "========================================================\n"
                    + f"Title: {current_node.title}\n"
                    + f"Release Date: {current_node.release_year}\n"
                    + f"Rating: {current_node.rating}\n"
                )
            current_node = current_node.next_movie_node
        return well_presented_data
    
    def get_data_by_release_year(self, start_year, end_year):
        start_year = int(start_year)
        end_year = int(end_year)
        result = []
        current_movie_node = self.head_node
        while current_movie_node:
            if current_movie_node.title is not None and start_year <= current_movie_node.release_year <= end_year:
                result.append(current_movie_node)
            current_movie_node = current_movie_node.next_movie_node
        return result

class MovieCollection:
    def __init__(self):
        self.genre_table = {}

    def get_movies_table(self):
        return self.genre_table

    def insert_movie(self, genre, title, release_year, rating):
        if genre not in self.genre_table:
            self.genre_table[genre] = MovieLinkedList()
        self.genre_table[genre].insert_beginning(title, release_year, rating)
    
    def get_movies_by_genre(self, genre):
        if genre in self.genre_table:
            return self.genre_table[genre].get_data()
        else:
            return "No movies found in this genre."