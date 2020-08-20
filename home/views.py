from django.shortcuts import render, get_object_or_404
from .models import Book
from profiles.models import UserProfile


# Create your views here.
def index(request):
    """ A view to return the index page """

    featured_books = Book.objects.filter(featured_item = True)
    recent_books = Book.objects.filter(date_added = "2020-07-16")
    
    user=request.user
    userprofile=None
    user_logged_in=False

    # Check if user is logged in
    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_logged_in=True

    context = {
        'featured_books': featured_books,
        'recent_books': recent_books,
        'user_logged_in': user_logged_in,
        # 'search_term': query,
    }

    return render(request, 'home/index.html', context)
