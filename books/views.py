from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Book, Category, Rating
from profiles.models import UserProfile, Hobby, Sport
from django.db.models import Q, Sum
from django.contrib import messages
from .filters import BookFilter
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO


def all_books(request):
    """ A view to show all books, including sorting and search queries """
    print('view triggered')
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
    user_logged_in=False
    already_rated=False
    user=request.user
    userprofile=None
    favorite=False

    # Check if user is logged in
    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_logged_in=True

    # Check if user has rated before
    ratings_for_this_book = Rating.objects.filter(book_id=current_book)
    if ratings_for_this_book.filter(rated_by=userprofile):
        already_rated=True

    # Check if book is in favorites
    user_favorites = userprofile.favorites.all()
   
    user_favorites_book_id = user_favorites.values('id')
    if user_favorites_book_id.filter(id=current_book):
        favorite=True
    
    # Grab all info about user and add this to rating instance
    if request.POST:
        ratingOptions = request.POST.get('ratingOptions')
        rated_by = request.POST.get('rated_by')
        book_id = get_object_or_404(Book, pk=book_id)
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_gender = userprofile.gender
        user_dob = userprofile.date_of_birth
        date_rating = datetime.now()
        age_rating = relativedelta(date_rating, user_dob)
        age_rating_years = age_rating.years
        age_rating_months = age_rating.months
        hobbies_rating = userprofile.hobbies.all()
        sports_rating = userprofile.sports.all()

        r = Rating(

            book_id=book_id, 
            rating=ratingOptions,
            gender=user_gender,
            rated_by=userprofile,
            age_rating_years=age_rating_years,
            age_rating_months=age_rating_months,
                                   
            )
        
        r.save()

        # Due to the nature of the m2m fields these need to be saved separately
        r.hobbies.set(hobbies_rating)
        r.sports.set(sports_rating)
 
    ratings_for_this_book = Rating.objects.filter(book_id=current_book)
    if ratings_for_this_book.filter(rated_by=userprofile):
        already_rated=True

    # All ratings by boys and girls
    rating = Rating.objects.filter(book_id=current_book)
    number_of_ratings = len(rating)
    total_rating_sum = rating.aggregate(sum=Sum('rating'))['sum']
    if number_of_ratings > 0:
        avg_rating = round(total_rating_sum / number_of_ratings, 1)
    else:
        avg_rating = 0    
    
    # Rating boys only
    boys_rating = Rating.objects.filter(book_id=current_book, gender='boy')
    boys_number_of_ratings = len(boys_rating)
    boys_total_rating_sum = boys_rating.aggregate(sum=Sum('rating'))['sum']
    if boys_number_of_ratings > 0:
        boys_avg_rating = round(boys_total_rating_sum / boys_number_of_ratings, 1)
    else:
        boys_avg_rating = 0    

    # Rating girls only
    girls_rating = Rating.objects.filter(book_id=current_book, gender='girl')
    girls_number_of_ratings = len(girls_rating)
    girls_total_rating_sum = girls_rating.aggregate(sum=Sum('rating'))['sum']
    if girls_number_of_ratings > 0:
        girls_avg_rating = round(girls_total_rating_sum / girls_number_of_ratings, 1)
    else:
        girls_avg_rating = 0    
    
    context = {
        'book': book,
        'rating': rating,
        'number_of_ratings': number_of_ratings,
        'avg_rating': avg_rating,
        'boys_avg_rating': boys_avg_rating,
        'girls_avg_rating': girls_avg_rating,
        'already_rated': already_rated,
        'favorite': favorite,
        'user_logged_in': user_logged_in,
        'boys_number_of_ratings': boys_number_of_ratings,
        'girls_number_of_ratings': girls_number_of_ratings,
    }

    return render(request, 'books/book_detail.html', context)


def add_to_favorites(request):
    
    book = get_object_or_404(Book, pk=book_id)
    current_book = book_id
    user_logged_in=False
    already_favorite=False
    
    # Check if user is logged in
    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_logged_in=True
    
    # # Check if book is already part of favorites
    # if userprofile.objects.filter(favorites=current_book):


    if already_favorite==False:
        UserProfile.favorites.update(book_id)
        print(UserProfile.favorites)
        already_favorite=True
        return redirect('book_detail', book_id=book_id)
    