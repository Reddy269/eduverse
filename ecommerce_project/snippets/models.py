from django.db import models

class Snippet(models.Model):
    title = models.CharField()
    code = models.TextField()

