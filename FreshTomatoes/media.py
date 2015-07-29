#Object to hold movie data
class Movie():

    def __init__(self, movie_title, movie_storyline, movie_rating, movie_producer, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.producer = movie_producer
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    
