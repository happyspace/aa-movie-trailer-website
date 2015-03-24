import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=KQUpZqshj7M")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                                   "The adventures of Gustave H, a legendary concierge at a famous hotel from the"
                                   " fictional Republic of Zubrowka between the first and second World Wars, and "
                                   "Zero Moustafa, the lobby boy who becomes his most trusted friend.",
                                   "http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                                   "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

winters_bone = media.Movie("Winter's Bone",
                           "An unflinching Ozark Mountain girl hacks through dangerous social"
                           " terrain as she hunts down her drug-dealing father while "
                           "trying to keep her family intact.",
                           "http://upload.wikimedia.org/wikipedia/en/6/6f/Winters_bone_poster.jpg",
                           "https://www.youtube.com/watch?v=5O8F8JtSVmI")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "When their relationship turns sour, a couple "
                               "undergoes a procedure to have each other erased "
                               "from their memories. But it is only through the "
                               "process of loss that they discover what they "
                               "had to begin with.",
                               "http://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=0zFywiAh7N0")

adele_blanc_sec = media.Movie("The Extraordinary Adventures of Adele Blanc-Sec",
                              "An adventure set in the early part of the 20th century"
                              " and focused on a popular novelist and her dealings "
                              "with would-be suitors, the cops, monsters, "
                              "and other distractions.",
                              "http://upload.wikimedia.org/wikipedia/en/d/da/Adele_Blanc-sec_Louise_Bourgoin_Luc_Besson.jpg",
                              "https://www.youtube.com/watch?v=DAhmCHnNcWs")

oldboy = media.Movie("Oldboy",
                     "After being kidnapped and imprisoned for 15 years, "
                     "Oh Dae-Su is released, only to find that he must "
                     "find his captor in 5 days.",
                     "http://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg",
                     "https://www.youtube.com/watch?v=tphnn5EPj2w")


the_one_i_love = media.Movie("The One I Love",
                             "Struggling with a marriage on the brink of falling apart, "
                             "a couple escapes for a weekend in pursuit of "
                             "their better selves, only to discover an unusual "
                             "dilemma that awaits them.",
                             "http://upload.wikimedia.org/wikipedia/en/4/41/TOIL_poster.jpg",
                             "https://www.youtube.com/watch?v=jCOvhojlZzQ")

movies = [grand_budapest_hotel, winters_bone, eternal_sunshine, adele_blanc_sec, oldboy, the_one_i_love]
fresh_tomatoes.open_movies_page(movies)

print (media.Movie.__doc__)
print (media.Movie.__name__)
# print (media.Movie.__class__)
print (media.Movie.__module__)
print (media.Movie.__dict__)