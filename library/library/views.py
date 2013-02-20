from django.views.generic import ListView, DetailView
from django.views.generic import YearArchiveView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Book, Author, Location

class BookListView(ListView):
    model = Book

class YearListView(ListView):
    queryset = Book.objects.order_by('year_published')

class ChangedBookListView(ListView):
    queryset = Book.objects.order_by('-modified')[:10]
    template_name = 'library/book_list_with_dates.html'

class NewBookListView(ListView):
    queryset = Book.objects.order_by('-created')[:10]
    template_name = 'library/book_list_with_dates.html'

class YearDetailView(YearArchiveView):
    queryset = Book.objects.all()
    allow_empty = True 
    allow_future = True
    date_field = 'year_published'
    make_object_list = True

class BookDetailView(DetailView):
    model = Book

class BookUpdateView(UpdateView):
    model = Book

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

class BookCreateView(CreateView):
    model = Book

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class LocationListView(ListView):
    model = Location

class LocationDetailView(DetailView):
    model = Location


