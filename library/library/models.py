from datetime import date

from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Location(TimeStampedModel):
    name = models.TextField(unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Author(TimeStampedModel):
    name = models.TextField(unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class Book(TimeStampedModel):
    origkey = models.CharField(max_length=36, blank=True, null=True)
    title = models.TextField()
    sortkey = models.TextField('Authors', blank=True)
    year_published = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    location = models.ForeignKey(Location, blank=True, null=True) 
        #    default=u'?', on_delete=models.SET_DEFAULT)
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ('sortkey', 'year_published', 'title')

    def __unicode__(self):
        return u'%s (%s): "%s"' % (self.sortkey, self.year_published, self.title) 

    def display_authors(self):
        if self.sortkey:
            return self.sortkey
        return u', '.join([a.name for a in self.authors.all()])

    def display_year_published(self):
        "We only care about the year"

        return self.year_published.strftime(u'%Y')

    def set_sortkey(self):
        "Generate a sortkey"

        if not self.sortkey and self.authors:
            self.sortkey = ', '.join([a.name for a in self.authors.all()])
            self.save()

    @staticmethod
    def from_dict(book):
        """Add a book from a dict. 

        Format of dict:
            title:      string
            year:       int or None
            authors:    list of strings
            location:   string
            sortkey:    string of authors in the order they appear on
                        the cover
            origkey:    (optional) original key, like an ISBN, or if
                        converting from another system
        """
        # Some books always go missing...
        location_string = book.get('location', u'?')
        location, _ = Location.objects.get_or_create(name=location_string)

        # Unknown years is okay
        year = book.get('year', None)
        try:
            int(year)
            year = date(year, 1, 1)
        except TypeError:
            year = None

        # Books can have more than one author, some have none
        author_ids = []
        for a in book.get('authors', []):
            author, created = Author.objects.get_or_create(name=a)
            author_ids.append(author.id)
        authors = Author.objects.filter(id__in=author_ids)

        # Make the book
        book, created = Book.objects.get_or_create(
                title=book['title'],
                year_published=year, 
                location=location, 
                origkey=book.get('origkey', None),
                sortkey=book.get('sortkey', u''),
        )

        # Add the authors
        for author in authors:
            book.authors.add(author)

        # Make a sortkey in case it is missing
        book.set_sortkey()

        return book
