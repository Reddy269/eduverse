import random
from django.core.management.base import BaseCommand
from ecommerce.models import Author, Book

class Command(BaseCommand):
    help = 'Seeds the database with 6 authors and 40 books'

    def handle(self, *args, **kwargs):
        Book.objects.all().delete()
        Author.objects.all().delete()

        authors_data = [
            {"name": "J.K. Rowling", "nationality": "British", "birth_year": 1965},
            {"name": "George R.R. Martin", "nationality": "American", "birth_year": 1948},
            {"name": "Agatha Christie", "nationality": "British", "birth_year": 1890},
            {"name": "Haruki Murakami", "nationality": "Japanese", "birth_year": 1949},
            {"name": "Chimamanda Ngozi Adichie", "nationality": "Nigerian", "birth_year": 1977},
            {"name": "Stephen King", "nationality": "American", "birth_year": 1947},
        ]

        authors = [Author.objects.create(**data) for data in authors_data]
        self.stdout.write(self.style.SUCCESS(f"Created {len(authors)} authors"))

        book_count = 0
        for author in authors:
            num_books = 40 // len(authors)  # distribute evenly (6*6=36, remainder handled below)
            for i in range(1, num_books + 1):
                Book.objects.create(
                    title=f"{author.name.split()[0]}'s Book {i}",
                    author=author,
                    published_year=random.randint(1970, 2023),
                    price=round(random.uniform(5, 50), 2)
                )
                book_count += 1

        # add remaining books (40 - 36 = 4) to random authors so total is exactly 40
        while book_count < 40:
            author = random.choice(authors)
            book_count += 1
            Book.objects.create(
                title=f"{author.name.split()[0]}'s Book {book_count}",
                author=author,
                published_year=random.randint(1970, 2023),
                price=round(random.uniform(5, 50), 2)
            )

        self.stdout.write(self.style.SUCCESS(f"Created {book_count} books"))