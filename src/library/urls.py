from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='library_home'),

    url(r'^search$', SearchView.as_view(), name='library_search'),

    url(r'^book/$', BookListView.as_view(), name='book_list'),
    url(r'^book/create/$', BookCreateView.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', BookUpdateView.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', BookDeleteView.as_view(), name='book_deete'),
    
    url(r'^year/$', YearListView.as_view(), name='year_list'),
    url(r'^changes/$', ChangedBookListView.as_view(), name='changed_book_list'),
    url(r'^new/$', NewBookListView.as_view(), name='new_book_list'),

    url(r'^author/$', AuthorListView.as_view(), name='author_list'),
    url(r'^location/$', LocationListView.as_view(), name='location_list'),

    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^year/(?P<year>\d{4})/$', YearDetailView.as_view(), name='year_detail'),

    url(r'^author/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),
    url(r'^location/(?P<pk>\d+)/$', LocationDetailView.as_view(), name='location_detail'),
)
