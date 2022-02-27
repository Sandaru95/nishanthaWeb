from django.db import models

from datetime import date

from authors.models import Author
from publishers.models import Publisher

class BookType(models.Model):
    title = models.CharField(max_length=150)
    title_sinhala = models.CharField(max_length=250, default=" ")

    def __str__(self):
        return str(self.title)

class Book(models.Model):
    title = models.CharField(max_length=100)
    title_sinhala = models.CharField(max_length=250, default=" ")
    cover = models.ImageField(upload_to="books/covers")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    isbn_number = models.CharField(max_length=100)
    stock_available = models.BooleanField(default=True)
    added_on = models.DateField(default=date.today)
    description = models.TextField(max_length=1000)
    no_visits = models.IntegerField(default=0)
    no_sales = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.publisher.title}"