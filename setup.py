from setuptools import setup

DJANGO_VERSION = "Django >= 1.5"
tests_require = [
        DJANGO_VERSION,
]

setup(
    name = 'django-library',
    version = '0.2',
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
    download_url = 'https://github.com/kaleissin/django-library/tarball/0.2#egg=django-library-0.2',

    package_dir = {'': 'src',},
    packages = ['library'],
    include_package_data = True,

    install_requires = [DJANGO_VERSION],
    tests_require = tests_require,
)
