from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Book, Category, Rating
from django.db.models import Q
from django.contrib import messages
from .filters import BookFilter

def all_books(request):
    """ A view to show all books, including sorting and search queries """
    
    # initiated from search in menu
    books = Book.objects.all() # Make sure this is a selection somehow (recent or popular). If There are 10K books in db, I do not want to show all...
    category = Category.objects.all()
    query = None
    search_results = False
    searched_term = None
    title_hit = None
    description_hit = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect (reverse('books'))
            
            queries =  Q(tags__name__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(author__icontains=query)| Q(gender__icontains=query) | Q(age__icontains=query)
            books = books.filter(queries).distinct()
            search_results = True
            searched_term=request.GET['q']

            # check what query was hit
            if books.filter(Q(title__icontains=query)):
                title_hit = searched_term
                print(title_hit)

            if books.filter(Q(description__icontains=query)):
                description_hit = searched_term
                print(description_hit)

    # initiated from search in menu
    # myFilter = BookFilter(request.GET, queryset=books)
    # books = myFilter.qs
    numResults = books.count()
    
    context = {
        'books': books,
        'search_term': query,
        'show_refine_bar': search_results,
        'categories': category,
        'numResults': numResults,
        'searched_term': searched_term,
        'title_hit': title_hit,
        'description_hit': description_hit,
    }

    return render(request, 'books/books.html', context)

def book_detail(request, book_id):
    """ A view to show book details """
    
    book = get_object_or_404(Book, pk=book_id)
    current_book = book_id

    rating = Rating.objects.filter(book_id=current_book)
    outcome = rating

    # def get_total_ratings(self):
    #         ratings = Rating.objects.filter(book_id=self)
    #         total_ratings = len(ratings)
    #         return total_ratings

    print(outcome)

    context = {
        'book': book,
        'outcome': outcome,
    }

    return render(request, 'books/book_detail.html', context)

def add_rating(request, rating_id):
    """ Test adding a rating """

    book = get_object_or_404(Book, pk=book_id)


