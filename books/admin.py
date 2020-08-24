from django.contrib import admin
from .models import Book, Category, Rating

# Register your models here.

class BookAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'isbn', 
        'title',
        'author',
        'category',
        'age',
    )

class CategoryAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'pk', 
        'name',
    )

admin.site.register(Book, BookAdmin) # 5.3 6.
admin.site.register(Category, CategoryAdmin) # 5.3 6.
admin.site.register(Rating)