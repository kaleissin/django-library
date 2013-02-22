from datetime import date

from django.test import TestCase
from django.db.models import fields

from library.models import Book, Author, Location

def diff_models(model1, model2, excludes=()):
    changes = {}
    for field in model1._meta.fields:
        if not (isinstance(field, (fields.AutoField, fields.related.RelatedField)) 
                or field.name in excludes):
            if field.value_from_object(model1) != field.value_from_object(model2):
                changes[field.verbose_name] = (field.value_from_object(model1),
                        field.value_from_object(model2))
    return changes

def diff_books(model1, model2):
    return diff_models(model1, model2, ('created', 'modified'))

class BookFromDictTestCase(TestCase):

    def setUp(self):
        testbook1 = Book.objects.create(
                title='Test 1', 
                sortkey='Author 1', 
                year_published=date(2013,1,1))
        self.testbook1 = testbook1

        testbook2 = Book(title='Test 2', sortkey='Author 2')
        self.testbook2 = testbook2

        testbook3 = Book.objects.create(
                title='Test 3', 
                sortkey='Author 3a, Author 3b')
        testbook3.authors.add(Author.objects.create(name="Author 3a"))
        testbook3.authors.add(Author.objects.create(name="Author 3b"))
        self.testbook3 = testbook3

        testbook4 = Book.objects.create(title='Test 4')
        testbook4.authors.add(Author.objects.create(name="Author 4a"))
        testbook4.authors.add(Author.objects.create(name="Author 4b"))
        testbook4.set_sortkey()
        self.testbook4 = testbook4

    def test_assertBook_from_dict_EqualYear(self):
        book = {
                'title': 'Test 1',
                'sortkey': 'Author 1', 
                'year': 2013,
        }
        newbook = Book.from_dict(book)
        self.assertEqual(diff_books(self.testbook1, newbook), {})
            
    def test_assertBook_from_dict_EqualNoYear(self):
        book = {
                'title': 'Test 2',
                'sortkey': 'Author 2', 
        }
        newbook = Book.from_dict(book)
        self.assertEqual(diff_books(self.testbook2, newbook), {})
            
    def test_assertBook_from_dict_AuthorsAndSortkey(self):
        book = {
                'title': 'Test 3',
                'sortkey': 'Author 3a, Author 3b', 
                'authors': ('Author 3a', 'Author 3b'), 
        }
        newbook = Book.from_dict(book)
        self.assertEqual(diff_books(self.testbook3, newbook), {})
            
    def test_assertBook_from_dict_AuthorsNoSortkey(self):
        book = {
                'title': 'Test 4',
                'authors': ('Author 4a', 'Author 4b'), 
        }
        newbook = Book.from_dict(book)
        self.assertEqual(diff_books(self.testbook4, newbook), {})
            
class BookTestCase(TestCase):

    def setUp(self):
        self.testbook1 = Book(title='Test 1', sortkey='Author 1', year_published=date(2013,1,1))

    def test_Book_display_authors(self):
        self.assertEqual(self.testbook1.sortkey, self.testbook1.display_authors())
