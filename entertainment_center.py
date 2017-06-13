import media

# Import webpage builder
import fresh_tomatoes

# Movies go here

toy_story = media.Movie(
    "Toy Story", "A story of a boy and "
    "his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uZNHIU3uHT4"
    )

dead_poets_society = media.Movie(
    "Dead Poets Society ",
    "English teacher John "
    "Keating inspires his students "
    "to look at poetry with a different "
    "perspective of authentic knowledge "
    "and feelings.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcSFiizcraYyxtIB2imVhFaWB5eMW1m95_Hp42MVj8Ngxo3Eq386",  # NOQA
    "https://www.youtube.com/watch?v=wrBk780aOis"
)

fargo = media.Movie(
    "Fargo",
    "Jerry Lundegaard's inept crime falls "
    "due to his and his henchmen's "
    "and the persistent police "
    "of the quite pregnant Marge Gunderson.",
    "http://img.moviepostershop.com/fargo-movie-poster-1996-1020194510.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6cJJjr8imTU"
    )

# Create a movies array which contains all movie objects

movies = [toy_story, avatar, dead_poets_society, fargo]

# Use fresh tomatoes to generate an HTML page with movies
fresh_tomatoes.open_movies_page(movies)
