import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imdb.settings')
django.setup()

from movies.models import Movie, Director


def populate_data():
    directors_data = [
        {'first_name': 'Christopher', 'last_name': 'Nolan', 'birth_year': 1970},
        {'first_name': 'Steven', 'last_name': 'Spielberg', 'birth_year': 1946},
        {'first_name': 'Martin', 'last_name': 'Scorsese', 'birth_year': 1942},
        {'first_name': 'Quentin', 'last_name': 'Tarantino', 'birth_year': 1963},
        {'first_name': 'James', 'last_name': 'Cameron', 'birth_year': 1954},
        {'first_name': 'Ridley', 'last_name': 'Scott', 'birth_year': 1937},
        {'first_name': 'David', 'last_name': 'Fincher', 'birth_year': 1962},
        {'first_name': 'Francis Ford', 'last_name': 'Coppola', 'birth_year': 1939},
        {'first_name': 'Peter', 'last_name': 'Jackson', 'birth_year': 1961},
        {'first_name': 'Sidney', 'last_name': 'Lumet', 'birth_year': 1924},
        {'first_name': 'Sergio', 'last_name': 'Leone', 'birth_year': 1929},
        {'first_name': 'Irvin', 'last_name': 'Kershner', 'birth_year': 1923},
        {'first_name': 'Robert', 'last_name': 'Zemeckis', 'birth_year': 1952},
        {'first_name': 'Frank', 'last_name': 'Darabont', 'birth_year': 1959},
    ]
    
    movies_data = [
        {'title': 'The Dark Knight', 'year': 2008, 'rank': 9, 'director_name': 'Christopher Nolan'},
        {'title': 'Inception', 'year': 2010, 'rank': 14, 'director_name': 'Christopher Nolan'},
        {'title': 'Forrest Gump', 'year': 1994, 'rank': 12, 'director_name': 'Robert Zemeckis'},
        {'title': 'The Shawshank Redemption', 'year': 1994, 'rank': 1, 'director_name': 'Frank Darabont'},
        {'title': 'Pulp Fiction', 'year': 1994, 'rank': 8, 'director_name': 'Quentin Tarantino'},
        {'title': 'The Matrix', 'year': 1999, 'rank': 15, 'director_name': None},
        {'title': 'Interstellar', 'year': 2014, 'rank': 29, 'director_name': 'Christopher Nolan'},
        {'title': 'Fight Club', 'year': 1999, 'rank': 11, 'director_name': 'David Fincher'},
        {'title': 'The Departed', 'year': 2006, 'rank': 44, 'director_name': 'Martin Scorsese'},
        {'title': 'Titanic', 'year': 1997, 'rank': 56, 'director_name': 'James Cameron'},
        {'title': 'Avatar', 'year': 2009, 'rank': 22, 'director_name': 'James Cameron'},
        {'title': 'Gladiator', 'year': 2000, 'rank': 43, 'director_name': 'Ridley Scott'},
        {'title': 'The Godfather', 'year': 1972, 'rank': 2, 'director_name': 'Francis Ford Coppola'},
        {'title': 'The Lord of the Rings: The Return of the King', 'year': 2003, 'rank': 7, 'director_name': 'Peter Jackson'},
        {'title': 'The Lord of the Rings: The Fellowship of the Ring', 'year': 2001, 'rank': 10, 'director_name': 'Peter Jackson'},
        {'title': 'Schindler\'s List', 'year': 1993, 'rank': 6, 'director_name': 'Steven Spielberg'},
        {'title': 'The Godfather: Part II', 'year': 1974, 'rank': 3, 'director_name': 'Francis Ford Coppola'},
        {'title': '12 Angry Men', 'year': 1957, 'rank': 5, 'director_name': 'Sidney Lumet'},
        {'title': 'The Good, the Bad and the Ugly', 'year': 1966, 'rank': 4, 'director_name': 'Sergio Leone'},
        {'title': 'Star Wars: Episode V - The Empire Strikes Back', 'year': 1980, 'rank': 13, 'director_name': 'Irvin Kershner'},
    ]
    
    print("Creating directors...")
    created_directors_count = 0
    for director_data in directors_data:
        director, created = Director.objects.get_or_create(
            first_name=director_data['first_name'],
            last_name=director_data['last_name'],
            defaults={'birth_year': director_data['birth_year']}
        )
        if created:
            created_directors_count += 1
            print(f"  Created director: {director}")
    
    print("\nCreating movies...")
    created_movies_count = 0
    for movie_data in movies_data:
        director_name = movie_data.pop('director_name')
        director = None
        if director_name:
            name_parts = director_name.split()
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:])
            try:
                director = Director.objects.get(first_name=first_name, last_name=last_name)
            except Director.DoesNotExist:
                print(f"  Warning: Director '{director_name}' not found")
        
        movie, created = Movie.objects.get_or_create(
            title=movie_data['title'],
            year=movie_data['year'],
            rank=movie_data['rank'],
            defaults={'director': director}
        )
        if created:
            created_movies_count += 1
            print(f"  Created movie: {movie} (Director: {director or 'None'})")
    
    print("\n" + "="*50)
    print("Data population complete!")
    print(f"Created {created_directors_count} new directors")
    print(f"Created {created_movies_count} new movies")
    print(f"Total directors in database: {Director.objects.count()}")
    print(f"Total movies in database: {Movie.objects.count()}")
    
    print("\nReverse relationship examples:")
    nolan = Director.objects.get(first_name='Christopher', last_name='Nolan')
    print(f"Movies directed by Christopher Nolan: {nolan.movies.count()}")
    for movie in nolan.movies.all():
        print(f"  - {movie}")


if __name__ == '__main__':
    populate_data()