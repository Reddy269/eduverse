from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(null=True, blank=True)
    age = models.SmallIntegerField()
    country = models.CharField(max_length = 50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name =  models.CharField(max_length = 150)
    price  =models.DecimalField(max_digits = 10, decimal_places= 2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'          # lets you do author.books.all()
    )
    published_year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title} by {self.author.name}"




