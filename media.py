import webbrowser

"""webbrowser is imported at the top of the program so that it can be called
later in the program to open a web browser"""

"""The class Movie is created, which will create a movie object, containing
the movie's title, story line, poster image and youtube trailer"""

class Movie():
    
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



    def show_trailer(self):
        """The show_trailer function is created below to open a web browser
        which will display a youtube trailer when a Movie object is called"""
        webbrowser.open(self.trailer_youtube_url)
