from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    birth_month = models.IntegerField(null=True, blank=True)
    birth_day = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'director'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rank = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True, related_name='movies')

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return f"{self.title} ({self.year})"
