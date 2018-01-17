from django.conf.urls import url

from . import views
from django.urls import path, re_path
# here we do our url mapping
urlpatterns = [
    path('', views.index, name='index'),
                        # implementing as class -- inherits from existing generic view
    path('books/', views.BookListView.as_view(), name='books'),

    # capture the book id, which must be an integer, and pass it to the view as a parameter named pk."""
    # you don't 'have' to name the datatype, this just ensures it."""
    # Important: The generic class-based detail view expects to be passed a parameter named pk. If you're writing your own function view you can use whatever parameter name you like, or indeed pass the information in an unnamed argument.

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # can also use regular expressions to match patterns

    #  	This is the RE used in our url mapper. It matches a string that has book/ at the start of the line (^book/), then has one or more digits (\d+), and then ends (with no non-digit characters before the end of line marker).

    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    # cant pass additional

    path('authors/', views.AuthorListView.as_view(), name='authors'),

    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]
