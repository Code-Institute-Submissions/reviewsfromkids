from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Book, Category, Rating
from profiles.models import UserProfile, Hobby, Sport
from django.db.models import Q, Sum, Count, Avg
from django.contrib import messages
from .filters import BookFilter
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO
from django.contrib.auth.decorators import login_required
from statistics import mode


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
    noresults = False
    # most_liked_by = None

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    
    numresults = books.count()
    
    # Grab search results to show context in template
    if request.GET:
        
        title__icontains = request.GET['title__icontains']
        author__icontains = request.GET['author__icontains']
        category = request.GET['category']
        most_liked_by = request.GET['most_liked_by']
        recommended_age__icontains = request.GET['recommended_age__icontains']
        rating = request.GET['rating']
        
        if not title__icontains and not author__icontains and not category and not most_liked_by and not recommended_age__icontains and not rating:
            search_performed = False
        else:
            search_performed = True

        if numresults == 0:
            noresults = True


    else:

        title__icontains = None
        author__icontains = None
        category = None
        most_liked_by = None
        recommended_age__icontains = None
        rating = None
        search_performed = False

    context = {

        'books': books,
        'search_term': query,
        'show_refine_bar': search_results,
        'categories': category,
        'numresults': numresults,
        'searched_term': searched_term,
        'title_hit': title_hit,
        'description_hit': description_hit,
        'myFilter': myFilter,
        'title': title__icontains,
        'author': author__icontains,
        'category': category,
        'most_liked_by': most_liked_by,
        'recommended_age__icontains': recommended_age__icontains,
        'rating': rating,
        'search_performed': search_performed,
        'noresults': noresults,

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
    user_logged_in = False
    already_rated = False
    user = request.user
    userprofile = None
    favorite = False
    recommended_age = None
    not_recommended_by_age = None
    rating = Rating.objects.filter(book_id=current_book)
        
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
            messages.success(request, f'Added to your list. Hope you will read it soon!')
            
            return redirect('book_detail', book_id=book_id)

    # Check if remove from favorites is in POST and remove from favorites
    if request.POST:
        if request.POST.get('type_of_action')=='remove_fav':
            userprofile.favorites.remove(current_book)
            messages.success(request, f'Removed from your list. Did you read it? Don\t forget to let other kids know if you liked it or not.')
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
            date_added=datetime.now(),
                                   
            )
        
        r.save()

        # Due to the nature of the m2m fields these need to be saved separately
        r.hobbies.set(hobbies_rating)
        r.sports.set(sports_rating)

        # Update ratings

        ## All ratings by boys and girls
        number_of_ratings = len(rating)
        total_rating_sum = rating.aggregate(sum=Sum('rating'))['sum']

        if number_of_ratings > 0:
            avg_rating = round(total_rating_sum / number_of_ratings, 1)
        else:
            avg_rating = 0.0
        
        ## Rating boys only
        boys_rating = Rating.objects.filter(book_id=current_book, gender='BOY')
        boys_number_of_ratings = len(boys_rating)
        boys_total_rating_sum = boys_rating.aggregate(sum=Sum('rating'))['sum']

        if boys_number_of_ratings > 0:
            boys_avg_rating = round(boys_total_rating_sum / boys_number_of_ratings, 1)
        else:
            boys_avg_rating = 0    

        ## Rating girls only
        girls_rating = Rating.objects.filter(book_id=current_book, gender='GIRL')
        girls_number_of_ratings = len(girls_rating)
        girls_total_rating_sum = girls_rating.aggregate(sum=Sum('rating'))['sum']

        if girls_number_of_ratings > 0:
            girls_avg_rating = round(girls_total_rating_sum / girls_number_of_ratings, 1)
        else:
            girls_avg_rating = 0

        # Who rated positive the most?
        # most_liked_by_girls = 'not known'

        if boys_number_of_ratings > girls_number_of_ratings:
            most_liked_by = 'boys'
        elif girls_number_of_ratings > boys_number_of_ratings:
            most_liked_by = 'girls'
        else:
            most_liked_by = 'boys and girls'
        
        # What age occurs most often in positive ratings? (mode not average)
        all_ages_rating = Rating.objects.filter(book_id=current_book, rating__gte=4)

        if all_ages_rating:
            all_ages_rating_years = all_ages_rating.values_list('age_rating_years') 
            age_mode = mode(all_ages_rating_years)
                        
            if age_mode:
                recommended_age = age_mode[0]
        
        else:
            recommended_age = 'not available'

        # What age occurs most often in positive ratings? (mode not average)
        all_ages_rating_low = Rating.objects.filter(book_id=current_book, rating__lte=2)

        if all_ages_rating_low:
            all_ages_rating_low_years = all_ages_rating_low.values_list('age_rating_years') 
            age_mode_low = mode(all_ages_rating_low_years)
                        
            if age_mode_low:
                not_recommended_by_age = age_mode_low[0]
        
        else:
            not_recommended_by_age = 'not available'
        
        Book.objects.update_or_create(
            pk=book.id,
            defaults={
                'rating': avg_rating,
                'number_of_ratings': number_of_ratings,
                'boys_avg_rating': boys_avg_rating,
                'boys_number_of_ratings': boys_number_of_ratings,
                'girls_avg_rating': girls_avg_rating,
                'girls_number_of_ratings': girls_number_of_ratings,
                'most_liked_by': most_liked_by,
                'recommended_age': recommended_age,
                'not_recommended_by_age': not_recommended_by_age,
            },
        )

        messages.success(request, f'Rated with a {ratingOptions}')

        # Redirect to prevent re-submitting
        book_id = book.id
        return redirect('book_detail', book_id=book_id)

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

    """Grab hobbies and sports connected to ratings of this book"""
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
    if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and avg_age_positive_ratings == None:
        no_positive_ratings_info = True
        if hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and avg_age_negative_ratings == None:   
            no_negative_ratings_info = True
            no_ratings_info_at_all = True
    
    if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and avg_age_positive_ratings == None and hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and avg_age_negative_ratings == None:   
        no_ratings_info_at_all = True       

    context = {

        'book': book,
        'rating': rating,
        'already_rated': already_rated,
        'favorite': favorite,
        'user_logged_in': user_logged_in,
        'avg_age_positive_ratings': avg_age_positive_ratings,
        'avg_age_negative_ratings': avg_age_negative_ratings,
        'recommended_age': recommended_age,
        'hobbies_positive_ratings': hobbies_positive_ratings,
        'hobbies_negative_ratings': hobbies_negative_ratings,
        'sports_positive_ratings': sports_positive_ratings,
        'sports_negative_ratings': sports_negative_ratings,
        'no_ratings_info_at_all': no_ratings_info_at_all,
    }

    return render(request, 'books/book_detail.html', context)
