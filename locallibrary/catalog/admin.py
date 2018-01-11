from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

# define admin class
# extends modelAdmin

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # removes empty inline spots

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    list_display_links = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_filter = ('last_name', 'first_name')
    #strange how it just knows the inline goes in the detail view
    inlines = [BooksInline]

# this decorater is the same as doing an admin.site.register(blah) below
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):      # django prevents manytomany fields here which is why display genre is created. display_genre is a function in the book model
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        ('meow', {
            'fields': ('book', 'imprint', 'id', 'book_language')
        }),
        ('Availability', {
            'fields': ('status', 'due_back',)
        }),
    )

admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
#admin.site.register(Author, AuthorAdmin)



