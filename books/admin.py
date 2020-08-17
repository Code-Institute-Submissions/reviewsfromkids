from django.contrib import admin
from .models import Book, Category, List, Rating

# Register your models here.

class BookAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'isbn', 
        'title',
        'author',
        'category',
        # 'tag', # gives error The value of 'list_display[4]' refers to 'tag', which is not a callable, an attribute of 'BookAdmin', or an attribute or method on 'books.Book'.
        # 'list', # idem
        'age',
        # 'rating_all',
        'image',
    )

    # ordering = ('rating_all',) # 6.4

class CategoryAdmin(admin.ModelAdmin): # 6.3
    list_display = (
        'friendly_name',
        'name',
    )

""" 
Removed tags and lists since this threw an error continuously when loading fixtures

class TagAdmin(admin.ModelAdmin): # 6.3
    list_display = (
        'friendly_name',
        'name',
    )

class ListAdmin(admin.ModelAdmin): # 6.3
    list_display = (
        'friendly_name',
        'name',
    ) """

admin.site.register(Book, BookAdmin) # 5.3 6.
admin.site.register(Category, CategoryAdmin) # 5.3 6.
admin.site.register(Rating)
""" admin.site.register(Tag, TagAdmin) # 5.3 6.
admin.site.register(List, ListAdmin) # 5.3 6. """