from django.shortcuts import render, redirect, reverse, get_object_or_404 # 10.5 import get_object_or_404
from .models import Book, Category # 7.2
from django.db.models import Q # 11.3
from django.contrib import messages
from .filters import BookFilter
# from django.views.generic import ListView

# Create your views here.

# 7.1
def all_books(request):
    """ A view to show all books, including sorting and search queries """
    
    # initiated from search in menu
    books = Book.objects.all() # Make sure this is a selection somehow (recent or popular). If There are 10K books in db, I do not want to show all...
    category = Category.objects.all()
    query = None
    search_results = False
    searched_term = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect (reverse('books'))
            
            queries =  Q(tags__name__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(author__icontains=query)| Q(gender__icontains=query) | Q(age__icontains=query)
            books = books.filter(queries).distinct()
            search_results = True

            # put searched terms into vars

            searched_term=request.GET['q']
            

    # initiated from search in menu
    # myFilter = BookFilter(request.GET, queryset=books)
    # books = myFilter.qs
    numResults = books.count()
    

    context = {
        'books': books,
        'search_term': query,
        'show_refine_bar': search_results,
        'categories': category,
        # 'myFilter': myFilter,
        'numResults': numResults,
        'searched_term': searched_term,
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
