from setuptools import setup

setup(
    name = 'django-library',
    version = '0.1',
    author = 'kaleissin',
    author_email = 'kaleissin@gmail.com',
    description = ('A django app for keeping score on '
            'what books you have and where they are'),
    long_description = open('README.rst').read(),
    classifiers = [
            'Development Status :: 3 - Alpha',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Topic :: Software Development :: Libraries',
    ],
    license = 'MIT',
    url = 'https://github.com/kaleissin/django-library',
    download_url = 'https://github.com/kaleissin/django-librardjango-library/tarball/0.1',

    package_dir = {'': 'src',},
    packages = ['library'],
    include_package_data = True,
)
