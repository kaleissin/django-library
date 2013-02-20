from django.views.generic import ListView, DetailView

from .models import Book, Author, Location

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class LocationListView(ListView):
    model = Location

class LocationDetailView(DetailView):
    model = Location
