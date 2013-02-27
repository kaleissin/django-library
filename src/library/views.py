import operator

from django.views.generic import ListView, DetailView
from django.views.generic import YearArchiveView
from django.views.generic import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from .models import Book, Author, Location

class SearchView(ListView):
    http_method_names = ('get',)
    template_name = 'library/search_results.html'
    model = Book

    def get_queryset(self):
        query = self.request.GET.get('q', u'').split()
        self.query = u' '.join(query)
        qs = self.model._default_manager
        if not query:
            return qs.none()
        q_objects = []
        for term in query:
            q_objects.append(Q(title__icontains=term))
            q_objects.append(Q(sortkey__icontains=term))
            q_objects.append(Q(location__name__icontains=term))

        q_objects = reduce(operator.or_, q_objects)
        return qs.select_related('location').filter(q_objects)

    def render_to_response(self, context, **response_kwargs):
        context['query'] = self.query
        return self.response_class(
                request = self.request,
                template = self.get_template_names(),
                context = context,
                **response_kwargs
        )

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


