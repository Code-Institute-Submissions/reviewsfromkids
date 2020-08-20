from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Book, Category, Rating
from profiles.models import UserProfile, Hobby, Sport
from django.db.models import Q, Sum, Count
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

    """ 
    A view for book details and to handle:
    - add and remove favorites
    - add rating
    - calculate ratings
    """
    
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

    
    """ Handle favorites """
    # Check if book is in favorites
    if user_logged_in:
        user_favorites = userprofile.favorites.all()
   
        user_favorites_book_id = user_favorites.values('id')
        if user_favorites_book_id.filter(id=current_book):
            favorite=True
    
    # Check if add to favorites is in POST and add to favorites
    if request.POST:
        if request.POST.get('type_of_action')=='add_fav':
            userprofile.favorites.add(current_book)
            return redirect('book_detail', book_id=book_id)

    # Check if remove from favorites is in POST and remove from favorites
    if request.POST:
        if request.POST.get('type_of_action')=='remove_fav':
            userprofile.favorites.remove(current_book)
            # show message with question why. If read, ask for rating.
            return redirect('book_detail', book_id=book_id)

    """ Handle ratings """
    # Check if user has rated before
    ratings_for_this_book = Rating.objects.filter(book_id=current_book)

    if ratings_for_this_book.filter(rated_by=userprofile):
        already_rated=True

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

        # Redirect to prevent re-submitting
        book_id = book.id
        return redirect('book_detail', book_id=book_id)
    
    """ Calculate ratings"""
    # If enough time: move to model as model methods

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
    boys_rating = Rating.objects.filter(book_id=current_book, gender='BOY')
    boys_number_of_ratings = len(boys_rating)
    boys_total_rating_sum = boys_rating.aggregate(sum=Sum('rating'))['sum']

    if boys_number_of_ratings > 0:
        boys_avg_rating = round(boys_total_rating_sum / boys_number_of_ratings, 1)
    else:
        boys_avg_rating = 0    

    # Rating girls only
    girls_rating = Rating.objects.filter(book_id=current_book, gender='GIRL')
    girls_number_of_ratings = len(girls_rating)
    girls_total_rating_sum = girls_rating.aggregate(sum=Sum('rating'))['sum']

    if girls_number_of_ratings > 0:
        girls_avg_rating = round(girls_total_rating_sum / girls_number_of_ratings, 1)
    else:
        girls_avg_rating = 0    
    
    """ Calculate avg age for ratings of this book """
    # Avg age for positive ratings
    positive_ratings = Rating.objects.filter(book_id=book_id, rating__gte=4)
    number_of_positive_ratings = len(positive_ratings)
    total_positive_ratings_years = positive_ratings.aggregate(sum=Sum('age_rating_years'))['sum']

    if number_of_positive_ratings > 0:
        avg_age_positive_ratings = round(total_positive_ratings_years / number_of_positive_ratings)
    else:
        avg_age_positive_ratings = None

    if avg_age_positive_ratings == 0:
        avg_age_positive_ratings = None

    # Avg age for negative ratings
    negative_ratings = Rating.objects.filter(book_id=book_id, rating__lte=2)
    number_of_negative_ratings = len(negative_ratings)
    total_negative_ratings_years = negative_ratings.aggregate(sum=Sum('age_rating_years'))['sum']
    
    if number_of_negative_ratings > 0:
        avg_age_negative_ratings = round(total_negative_ratings_years / number_of_negative_ratings)
    else:
        avg_age_negative_ratings = None
    
    if avg_age_negative_ratings == 0:
        avg_age_negative_ratings = None

    """ Grab hobbies and sports connected to ratings of this book """
    # if user_logged_in:
    #     user_hobbies = Hobby.objects.filter(userprofile__user=request.user)
    #     user_sports = Sport.objects.filter(userprofile__user=request.user)

    # Hobbies and positive ratings
    all_hobbies_of_positive_ratings = Hobby.objects.filter(rating__book_id=book_id, rating__rating__gte=4)
    hobbies_positive_ratings = all_hobbies_of_positive_ratings.values('name').annotate(Count('name')).order_by('-name__count')[:2]
    
    # Hobbies and negative ratings
    all_hobbies_of_negative_ratings = Hobby.objects.filter(rating__book_id=book_id, rating__rating__lte=2)
    hobbies_negative_ratings = all_hobbies_of_negative_ratings.values('name').annotate(Count('name')).order_by('-name__count')[:2]

    # Sports and positive ratings
    all_sports_of_positive_ratings = Sport.objects.filter(rating__book_id=book_id, rating__rating__gte=4)
    sports_positive_ratings = all_sports_of_positive_ratings.values('name').annotate(Count('name')).order_by('-name__count')[:2]

    # Sports and negative ratings
    all_sports_of_negative_ratings = Sport.objects.filter(rating__book_id=book_id, rating__rating__lte=2)
    sports_negative_ratings = all_sports_of_negative_ratings.values('name').annotate(Count('name')).order_by('-name__count')[:2]
    
    
    # In case of a new book or a book without ratings infornation
    no_ratings_info_at_all = False
    # if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and avg_age_positive_ratings == None:
    #     no_positive_ratings_info = True
    #     if hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and avg_age_negative_ratings == None:   
    #         no_negative_ratings_info = True
    #         no_ratings_info_at_all = True
    
    
    if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and avg_age_positive_ratings == None and hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and avg_age_negative_ratings == None:   
        no_ratings_info_at_all = True
    print('no ratings at all:', no_ratings_info_at_all)
    
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
        'avg_age_positive_ratings': avg_age_positive_ratings,
        'avg_age_negative_ratings': avg_age_negative_ratings,
        # 'user_hobbies': user_hobbies,
        # 'user_sports': user_sports,
        'hobbies_positive_ratings': hobbies_positive_ratings,
        'hobbies_negative_ratings': hobbies_negative_ratings,
        'sports_positive_ratings': sports_positive_ratings,
        'sports_negative_ratings': sports_negative_ratings,
        'no_ratings_info_at_all': no_ratings_info_at_all,
    }

    return render(request, 'books/book_detail.html', context)
