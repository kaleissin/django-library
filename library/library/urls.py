from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView

from .views import *

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='library_home'),
    url(r'^book/$', BookListView.as_view(), name='book_list'),
    url(r'^author/$', AuthorListView.as_view(), name='author_list'),
    url(r'^location/$', LocationListView.as_view(), name='location_list'),

    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),
    url(r'^location/(?P<pk>\d+)/$', LocationDetailView.as_view(), name='location_detail'),
)
