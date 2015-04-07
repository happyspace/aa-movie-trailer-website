import webbrowser

class Movie():
    """
    This class provides a way to store movie related information
    """
    # valid ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube,
                 movie_rating='NR',
                 movie_director='',
                 movie_year=0,
                 movie_duration='',
                 staring=(),
                 ):

        """


        :type movie_rating: str
        :param movie_title: movie title
        :param movie_storyline: movie caption
        :param poster_image: movie poster image
        :param trailer_youtube: a youtube trailer for the movie
        :param movie_rating: movie rating
        :param movie_director: movie director
        :param movie_year: movie year
        :param movie_duration: movie duration
        :param staring: a tuple of main actors
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # optional attributes
        self.movie_rating = movie_rating
        self.movie_director = movie_director
        self.movie_year = movie_year


