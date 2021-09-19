from django.contrib import admin
from .models import Author, Publisher, BookType, Book

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookType)
admin.site.register(Book)