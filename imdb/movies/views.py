from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie
from .utils import print_queries



def get_movies(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET['limit'])
    
    movies = Movie.objects.all()[offset:offset + limit]
    
    movies_data = []
    for movie in movies:
        movies_data.append({
            'id': movie.id,
            'title': movie.title,
            'year': movie.year,
            'rank': movie.rank
        })
    
    return JsonResponse({
        'movies': movies_data,
        'total': Movie.objects.count()
    })
