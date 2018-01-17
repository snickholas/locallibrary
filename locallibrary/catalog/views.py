from multiprocessing import context

from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


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
    num_instances_available = BookInstance.objects.filter(status='a').count()
    # __exact and __iexact both options. = is also an option, suppose its the same as exact
    total_eng_inst = BookInstance.objects.filter(book_language__iexact='english').count()
    # __ used to trace back through models.
    # many book instances are of one book. one book has many genres.
    total_fict_inst = BookInstance.objects.filter(book__genre__name='Fiction').count()
    num_authors = Author.objects.count()  # the all() is implied by default

    # render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        # dictionary containing the data that will be inserted into those placeholders
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'total_eng_inst': total_eng_inst, 'total_fict_inst': total_fict_inst},
    )


# a generic view defined by django used to list objects
class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

    # context_object_name = 'my_book_list'  # your own name for the list as a template variable
    # queryset = Book.objects.filter(genre__name='Fiction')[:5]  # Get 5 books containing the title war
     # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

    # can override the queryset method and change what is default returned


    """For example, we can override the  get_queryset() method to change the list of records returned. This is more flexible than just setting the queryset attribute as we did in the preceding code fragment (though there is no real benefit in this case):"""
    #def get_queryset(self):
     #   return Book.objects.filter(genre__icontains='fiction')[:5]


    """We might also override get_context_data() in order to pass additional context variables to the template (e.g. the list of books is passed by default). The fragment below shows how to add a variable named "some_data" to the context (it would then be available as a template variable)."""
 #   def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
    #    context = super(BookListView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
   #     context['some_data'] = 'This is just some data'
        # return the new updated context
    #    return context

class BookDetailView(generic.DetailView):
    model = Book

# if, for example, we weren't using the generic class based views, you could define something similar as the following:

"""def book_detail_view(request, pk):
    try:
        book_id = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    # shortcut for raising a 404 if no record found (also a get_list variant)
    # book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'catalog/book_detail.html',
        context={'book': book_id, }
    ) """