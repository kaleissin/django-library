==============
django-library
==============

A simple library app for Django 1.5, where "Library" is defined as "a
collection of books", not "a place to read/borrow books".

The *app* itself is ``library``.

For an example project incorporating the app, see
``homelibrary`` in the source.


Installation of Dependencies
============================

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

Using the app
=============

Pop the ``library`` directory into your python path, for instance with
pip: "pip install django-library". Then append "library" to your
INSTALLED_APPS. The included templates look for a template "base.html",
see the one in homelibrary/templates for an example.

Run south to add tables::

    $ ./manage.py migrate library

Test driving the example project
================================

Set up a virtualenv with django (not tested with Django 1.6 yet),
activate it; download the entire "django-library" directory somehow,
then ``cd`` into the same directory as the Makefile and run::

    $ export SECRET_KEY='foo'
    $ make cmd CMD="migrate library"
    $ make cmd CMD=runserver

... and hop on over to http://127.0.0.1/admin to play around.
