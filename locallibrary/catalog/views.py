from multiprocessing import context

from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# View functions to get the requested data from the models, create an HTML page displaying the data, and return it to the user to view in the browser.
# Create your views here.

def index(request):
    """
    view function for the home page of the site
    :param request:
    :return:
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    total_eng_inst = BookInstance.objects.filter(book_language__iexact='english').count()
    total_fict_inst = BookInstance.book
    num_authors = Author.objects.count() #the all() is implied by default

    #render the html template index.html with the data in the context variable

    return render(
        request,
        'index.html',
        # dictionary containing the data that will be inserted into those placeholders
        context={'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors, 'total_eng_inst': total_eng_inst, 'total_fict_inst': total_fict_inst},
    )



