import media
import fresh_tomatoes

"""
This class encapsulates the movie data for the web site.

Style note: Movie instantiation should use keyword
attribute names for both mandatory and optional attributes.

"""
grand_budapest_hotel = media.Movie(movie_title="The Grand Budapest Hotel",
                                   movie_storyline="The adventures of Gustave H, a legendary concierge at a famous hotel from the"
                                   " fictional Republic of Zubrowka between the first and second World Wars, and "
                                   "Zero Moustafa, the lobby boy who becomes his most trusted friend.",
                                   poster_image="http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                                   trailer_youtube="https://www.youtube.com/watch?v=1Fg5iWmQjwk",
                                   movie_year=2014)

winters_bone = media.Movie(movie_title="Winter's Bone",
                           movie_storyline="An unflinching Ozark Mountain girl hacks through dangerous social"
                           " terrain as she hunts down her drug-dealing father while "
                           "trying to keep her family intact.",
                           poster_image="http://upload.wikimedia.org/wikipedia/en/6/6f/Winters_bone_poster.jpg",
                           trailer_youtube="https://www.youtube.com/watch?v=5O8F8JtSVmI",
                           movie_year=2010)

eternal_sunshine = media.Movie(movie_title="Eternal Sunshine of the Spotless Mind",
                               movie_storyline="When their relationship turns sour, a couple "
                               "undergoes a procedure to have each other erased "
                               "from their memories. But it is only through the "
                               "process of loss that they discover what they "
                               "had to begin with.",
                               poster_image="http://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               trailer_youtube="https://www.youtube.com/watch?v=0zFywiAh7N0",
                               movie_year=2004)

adele_blanc_sec = media.Movie(movie_title="The Extraordinary Adventures of Adele Blanc-Sec",
                              movie_storyline="An adventure set in the early part of the 20th century"
                              " and focused on a popular novelist and her dealings "
                              "with would-be suitors, the cops, monsters, "
                              "and other distractions.",
                              poster_image="http://upload.wikimedia.org/wikipedia/en/d/da/Adele_Blanc-sec_Louise_Bourgoin_Luc_Besson.jpg",
                              trailer_youtube="https://www.youtube.com/watch?v=DAhmCHnNcWs",
                              movie_year=2010)

oldboy = media.Movie(movie_title="Oldboy",
                     movie_storyline="After being kidnapped and imprisoned for 15 years, "
                     "Oh Dae-Su is released, only to find that he must "
                     "find his captor in 5 days.",
                     poster_image="http://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg",
                     trailer_youtube="https://www.youtube.com/watch?v=tphnn5EPj2w",
                     movie_year=2003)


the_one_i_love = media.Movie(movie_title="The One I Love",
                             movie_storyline="Struggling with a marriage on the brink of falling apart, "
                             "a couple escapes for a weekend in pursuit of "
                             "their better selves, only to discover an unusual "
                             "dilemma that awaits them.",
                             poster_image="http://upload.wikimedia.org/wikipedia/en/4/41/TOIL_poster.jpg",
                             trailer_youtube="https://www.youtube.com/watch?v=jCOvhojlZzQ",
                             movie_year=2014)

# movies collection
movies = [grand_budapest_hotel, winters_bone, eternal_sunshine, adele_blanc_sec, oldboy, the_one_i_love]

# create web page
fresh_tomatoes.open_movies_page(movies)

