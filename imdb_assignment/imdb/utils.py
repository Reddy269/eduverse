from .models import Director, Movie, Cast, Ratings, Actor


def populate_database(
        actors_list, movies_list, directors_list, movie_rating_list):
    """
    :param actors_list:[
        {
            "actor_id": "actor_1",
            "name": "Actor 1"
        }
    ]
    :param movies_list: [
        {
            "movie_id": "movie_1",
            "name": "Movie 1",
            "actors": [
                {
                    "actor_id": "actor_1",
                    "role": "hero",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "12.3",
            "release_date": "2020-3-3",
            "director_name": "Director 1"
        }
    ]
    :param directors_list: [
        "Director 1"
    ]
    :param movie_rating_list: [
        {
            "movie_id": "movie_1",
            "rating_one_count": 4,
            "rating_two_count": 4,
            "rating_three_count": 4,
            "rating_four_count": 4,
            "rating_five_count": 4
        }
    ]
    """
    for director in directors_list:
        Director.objects.create(
            name=director
        )

    for actor in actors_list:
        Actor.objects.create(
            name=actor["name"],
            actor_id=actor["actor_id"],
        )

    for movie in movies_list:

        director = Director.objects.get(name=movie["director_name"])

        Movie.objects.create(
            movie_id=movie["movie_id"],
            name=movie["name"],
            release_date=movie["release_date"],
            box_office_collection_in_crores=movie["box_office_collection_in_crores"],
            director=director
        )
        movie_id = movie["movie_id"]
        for actor in movie["actors"]:
            Cast.objects.create(
                actor_id=actor["actor_id"],
                movie_id=movie_id,
                role=actor["role"],
                is_debut_movie=actor["is_debut_movie"]
            )
    for ratings in movie_rating_list:
        Ratings.objects.create(
        movie_id = ratings["movie_id"],
        rating_one_count = ratings["rating_one_count"],
        rating_two_count = ratings["rating_two_count"],
        rating_three_count = ratings["rating_three_count"],
        rating_four_count = ratings["rating_four_count"],
        rating_five_count = ratings["rating_five_count"]
        )


def get_no_of_distinct_movies_actor_acted(actor_id):

    actor = Actor.objects.get(pk=actor_id)
    return Movie.objects.filter(cast__actor = actor).distinct().count()

def get_movies_directed_by_director(director_obj):

    Movie.objects.filter(director = director_obj).values('name')








