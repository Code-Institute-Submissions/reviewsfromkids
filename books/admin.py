from django.contrib import admin
from .models import Book, Category, Rating

# Register your models here.

class BookAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'pk',
        'isbn', 
        'title',
        'author',
        'category',
        'rating',
        'age_on_book',
        'not_recommended_by_age',
        'recommended_age',
        'most_liked_by'
    )

class CategoryAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'pk', 
        'name',
    )

class RatingAdmin(admin.ModelAdmin): #6.2
    list_display = (
        'pk', 
        'age_rating_years',
        'rating',
        'gender',
        'book_id',
    )

admin.site.register(Book, BookAdmin) # 5.3 6.
admin.site.register(Category, CategoryAdmin) # 5.3 6.
admin.site.register(Rating, RatingAdmin)