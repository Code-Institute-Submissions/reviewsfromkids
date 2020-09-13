from django.contrib import admin

from .models import Book, Category, Rating


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'isbn',
        'title',
        'author',
        'category',
        'rating',
        'number_of_ratings',
        'age_on_book',
        'not_recommended_by_age',
        'recommended_age',
        'most_liked_by',
        'most_disliked_by',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'age_rating_years',
        'rating',
        'gender',
        'book_id',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
