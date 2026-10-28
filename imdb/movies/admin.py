from django.contrib import admin
from .models import Movie, Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_year')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'rank', 'director')
    list_filter = ('year', 'director')
    search_fields = ('title', 'director__first_name', 'director__last_name')
    ordering = ('rank', 'year', 'title')
