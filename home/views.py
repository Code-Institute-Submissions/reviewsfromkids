from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    """ A view to return the index page """

    featured_books = Book.objects.filter(featured_item = True)
    recent_books = Book.objects.filter(date_added = "2020-07-16")

    context = {
        'featured_books': featured_books,
        'recent_books': recent_books,
        # 'search_term': query,
    }

    return render(request, 'home/index.html', context)