from django.contrib import admin
from .models import BookType, Book

admin.site.register(BookType)
admin.site.register(Book)