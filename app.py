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