from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE, null=True, blank=True)

class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Actor(models.Model):
    actor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

class Cast(models.Model):
    cast_id = models.CharField(max_length=100)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE, null=True, blank=True)
    is_debut_movie = models.BooleanField(default=False)
    role = models.CharField(max_length=50)

class Ratings(models.Model):
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, null=True, blank=True)
    rating_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating_one_count = models.IntegerField(choices=rating_choices, default=0)
    rating_two_count = models.IntegerField(choices=rating_choices, default=0)
    rating_three_count = models.IntegerField(choices=rating_choices, default=0)
    rating_four_count = models.IntegerField(choices=rating_choices, default=0)
    rating_five_count = models.IntegerField(choices=rating_choices, default=0)

