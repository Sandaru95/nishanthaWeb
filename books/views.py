from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from .models import Book, BookType

class IndexView(TemplateView):
    template_name = "books/index.html"

class DetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'books/detail.html', {'book': book})
