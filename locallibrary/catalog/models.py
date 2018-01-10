from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
# these will be associated to database tables. django is fancy-huh and creates them all on the fly
# must remember whenever there is a change to a model (like adding attributes and such) we have to py -3 manage.py makemigrations and ' ' migrate
# this generates the ddl necessary for updating the model

class Genre(models.Model):
    """
    model for representing a book genre
    """
    name = models.CharField(max_length=200, help_text="enter a book genre")

    def __str__(self):
        """
        string representing the mode object (in admin site )
        """
        return self.name

class Book(models.Model):
    """
    model representing a book, not a specific instance of a book
    """
    title = models.CharField(max_length=200)
                                #author has to be a string here since its class has not yet been defined .. why?
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    # removed quotes in second version on the book object .. test out difference
    # book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    # tuple containing tuples of key-value pairs
    # assuming using this just so it will never be changed
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # language model - challenge
    # adding language as an attribute of an instance of a book. For example, a dictionary can be written in multiple languages
    # for easiness sake, including multiple languages and an 'other' option to catch all. Could be better implemented
    language = (
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('Mandarin', 'Mandarin'),
        ('French', 'French'),
        ('Yiddish', 'Yiddish'),
        ('German', 'German'),
        ('Russian', 'Russian'),
        ('Pig Latin', 'Pig Latin'),
        ('Other', 'Other'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')
    book_language = models.CharField(max_length=10, choices=language, help_text='language this book is written in', default='English')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id, self.book.title)

class Author(models.Model):
        """
        Model representing an author.
        """
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField('Died', null=True, blank=True)

        class Meta:
            ordering = ["last_name", "first_name"]

        def get_absolute_url(self):
            """
            Returns the url to access a particular author instance.
            """
            return reverse('author-detail', args=[str(self.id)])

        def __str__(self):
            """
            String for representing the Model object.
            """
            return '{0}, {1}'.format(self.last_name, self.first_name)