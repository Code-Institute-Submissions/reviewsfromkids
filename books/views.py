from django.shortcuts import render, get_object_or_404 # 10.5 import get_object_or_404
from .models import Book # 7.2
from django.views.generic import ListView

# Create your views here.

# 7.1
def all_books(request):
    """ A view to show all books, including sorting and search queries """
    
    # 7.3 grab all products from the database and put it in products
    books = Book.objects.all() 

    # 7.4 make the books available for the template by adding this to the context
    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)

# 10.1
def book_detail(request, book_id): #10.2 Add the book.id as parameter
    """ A view to show book details """
    
    # 10.3 get one product based on id
    book = get_object_or_404(Book, pk=book_id)

    # 10.4 make the product available for the template by adding this to the context
    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
