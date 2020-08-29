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
import math


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
    recommended_age_boys = None
    recommended_age_girls = None
    not_recommended_by_age_boys = None
    not_recommended_by_age_girls = None
    # most_liked_by = None
    # most_disliked_by = None
    user = request.user
    userprofile = None
    user_favorites_id = None

    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_favorites_id = []
        # user_favorites_id = userprofile.favorites.values("id")
        a =  userprofile.favorites.values("id")
        for id in a:
            user_favorites_id.append(id["id"])

    # Search
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
        'userprofile': userprofile,
        'user_favorites_id': user_favorites_id,

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
    allowed_to_rate = False
    user = request.user
    userprofile = None
    favorite = False
    recommended_age = None
    not_recommended_by_age = None
    recommended_age_boys = None
    not_recommended_by_age_boys = None
    recommended_age_girls = None
    not_recommended_by_age_girls = None
    current_user_rating = None
    rating = Rating.objects.filter(book_id=current_book)
    most_liked_by = None
    most_disliked_by = None
    age_mode = None
    age_mode_low = None
    age_mode_boys_positive = None
    age_mode_boys_negative = None
    age_mode_girls_positive = None
    age_mode_girls_negative = None

        
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
            messages.info(request, f'Removed from your list. Did you read it? Let other kids know whether you liked it or not!')
            return redirect('book_detail', book_id=book_id)

    """ Handle ratings """
    # Check if user is allowed to rate
    if user_logged_in:
        if userprofile.profile_complete == 'lvl-0':
            allowed_to_rate = False
        else:
            allowed_to_rate = True

    # Check if user has rated before
    ratings_for_this_book = Rating.objects.filter(book_id=current_book)

    if ratings_for_this_book.filter(rated_by=userprofile):
        already_rated=True
        userprofile = get_object_or_404(UserProfile, user=request.user)
        current_user_rating = get_object_or_404(Rating, book_id=book_id, rated_by=userprofile)

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

        if request.POST.get('type_of_action')=='new':

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

            messages.success(request, f'Rated with a {ratingOptions}')

            # Due to the nature of the m2m fields these need to be saved separately
            r.hobbies.set(hobbies_rating)
            r.sports.set(sports_rating)

        if request.POST.get('type_of_action')=='edit':

            Rating.objects.update_or_create(

                book_id=book.id,
                rated_by=userprofile,

                defaults={

                'rating': ratingOptions,

                },
            )

            messages.success(request, f'Rating changed to {ratingOptions}')

        if request.POST.get('type_of_action')=='delete':

            current_user_rating.delete()
            
            messages.success(request, f'Rating deleted')

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
        boys_rating_positive = Rating.objects.filter(book_id=current_book, gender='BOY', rating__gte=4)
        boys_number_of_ratings_positive = len(boys_rating_positive)

        girls_rating_positive = Rating.objects.filter(book_id=current_book, gender='GIRL', rating__gte=4)
        girls_number_of_ratings_positive = len(girls_rating_positive)

        if boys_number_of_ratings_positive > girls_number_of_ratings_positive:
            most_liked_by = 'boys'
        elif girls_number_of_ratings_positive > boys_number_of_ratings_positive:
            most_liked_by = 'girls'
        elif girls_number_of_ratings_positive == 0 and boys_number_of_ratings_positive == 0:
            most_liked_by = 'not known yet'
        else:
            most_liked_by = 'all, this most be really good!'
        
        # Who rated negative the most?
        boys_rating_negative = Rating.objects.filter(book_id=current_book, gender='BOY', rating__lte=2)
        boys_number_of_ratings_negative = len(boys_rating_negative)

        girls_rating_negative = Rating.objects.filter(book_id=current_book, gender='GIRL', rating__lte=2)
        girls_number_of_ratings_negative = len(girls_rating_negative)

        if boys_number_of_ratings_negative > girls_number_of_ratings_negative:
            most_disliked_by = 'boys'
        elif girls_number_of_ratings_negative > boys_number_of_ratings_negative:
            most_disliked_by = 'girls'
        elif girls_number_of_ratings_negative == 0 and boys_number_of_ratings_negative == 0:
            most_disliked_by = 'not known yet'
        else:
            most_disliked_by = 'all, this most be really bad...'
        
        # What age occurs most often in positive ratings? (mode not average)
        all_ages_rating = Rating.objects.filter(book_id=current_book, rating__gte=4)
        
        if all_ages_rating:
            all_ages_rating_years = all_ages_rating.values_list('age_rating_years')
            
            try:
                age_mode = mode(all_ages_rating_years)
            
            except:
                recommended_age = 'not available'
                        
            if age_mode:
                recommended_age = age_mode[0]
        
        else:
            recommended_age = 'not available'
        
        # What age occurs most often in negative ratings? (mode not average)
        all_ages_rating_low = Rating.objects.filter(book_id=current_book, rating__lte=2)

        if all_ages_rating_low:
            all_ages_rating_low_years = all_ages_rating_low.values_list('age_rating_years')

            try:
                age_mode_low = mode(all_ages_rating_low_years)
            
            except:
                not_recommended_by_age = 'not available'

            if age_mode_low:
                not_recommended_by_age = age_mode_low[0]
            
        else:
            not_recommended_by_age = 'not available'
        
        # Handle round up to halfs for display as stars
        star_rating_all = (math.ceil(2*avg_rating))/2
        star_rating_boys = (math.ceil(2*boys_avg_rating))/2
        star_rating_girls = (math.ceil(2*girls_avg_rating))/2

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
                'most_disliked_by': most_disliked_by,
                'recommended_age': recommended_age,
                'not_recommended_by_age': not_recommended_by_age,
                'star_rating_all': star_rating_all,
                'star_rating_boys': star_rating_boys,
                'star_rating_girls': star_rating_girls,
            },
        )
        
        # Redirect to prevent re-submitting
        book_id = book.id
        return redirect('book_detail', book_id=book_id)
    
    """ Calculate mode age for ratings of this book by gender"""
    # Mode age for positive ratings boys
    all_ages_rating_boys_positive = Rating.objects.filter(book_id=current_book, rating__gte=4, gender='BOY')
    
    if all_ages_rating_boys_positive:
        all_ages_rating_boys_positive_years = all_ages_rating_boys_positive.values_list('age_rating_years') 
        
        try:
            age_mode_boys_positive = mode(all_ages_rating_boys_positive_years)
        
        except:
            recommended_age_boys = 'not available'
                        
    if age_mode_boys_positive:
        recommended_age_boys = age_mode_boys_positive[0]
        
    else:
        recommended_age_boys = 'not available'

    # Mode age for negative ratings boys
    all_ages_rating_boys_negative = Rating.objects.filter(book_id=current_book, rating__lte=2, gender='BOY')
    if all_ages_rating_boys_negative:
        all_ages_rating_boys_negative_years = all_ages_rating_boys_negative.values_list('age_rating_years') 
        
        try:
            age_mode_boys_negative = mode(all_ages_rating_boys_negative_years)

        except:
            not_recommended_by_age_boys = 'not available'
                        
    if age_mode_boys_negative:
        not_recommended_by_age_boys = age_mode_boys_negative[0]
    
    else:
        not_recommended_by_age_boys = 'not available'

    # Mode age for positive ratings girls
    all_ages_rating_girls_positive = Rating.objects.filter(book_id=current_book, rating__gte=4, gender='GIRL')
    if all_ages_rating_girls_positive:
        all_ages_rating_girls_positive_years = all_ages_rating_girls_positive.values_list('age_rating_years') 
        
        try:
            age_mode_girls_positive = mode(all_ages_rating_girls_positive_years)

        except:
            recommended_age_girls = 'not available'
                        
    if age_mode_girls_positive:
        recommended_age_girls = age_mode_girls_positive[0]
    
    else:
        recommended_age_girls = 'not available'
    
    # Mode age for negative ratings girls
    all_ages_rating_girls_negative = Rating.objects.filter(book_id=current_book, rating__lte=2, gender='GIRL')
    if all_ages_rating_girls_negative:
        all_ages_rating_girls_negative_years = all_ages_rating_girls_negative.values_list('age_rating_years') 
        
        try:
            age_mode_girls_negative = mode(all_ages_rating_girls_negative_years)
        
        except:
            not_recommended_by_age_girls = 'not available'
                        
    if age_mode_girls_negative:
        not_recommended_by_age_girls = age_mode_girls_negative[0]
    
    else:
        not_recommended_by_age_girls = 'not available'

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
    if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and recommended_age == None:
        no_positive_ratings_info = True
        if hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and not_recommended_by_age == None:   
            no_negative_ratings_info = True
            no_ratings_info_at_all = True
    
    if hobbies_positive_ratings.exists()==False and sports_positive_ratings.exists()==False and recommended_age == None and hobbies_negative_ratings.exists()==False and sports_negative_ratings.exists()==False and not_recommended_by_age == None:   
        no_ratings_info_at_all = True

    context = {

        'book': book,
        'rating': rating,
        'current_user_rating': current_user_rating,
        'already_rated': already_rated,
        'favorite': favorite,
        'user_logged_in': user_logged_in,
        'recommended_age': recommended_age,
        'hobbies_positive_ratings': hobbies_positive_ratings,
        'hobbies_negative_ratings': hobbies_negative_ratings,
        'sports_positive_ratings': sports_positive_ratings,
        'sports_negative_ratings': sports_negative_ratings,
        'no_ratings_info_at_all': no_ratings_info_at_all,
        'not_recommended_by_age_girls': not_recommended_by_age_girls,
        'recommended_age_girls': recommended_age_girls,
        'not_recommended_by_age_boys': not_recommended_by_age_boys,
        'recommended_age_boys': recommended_age_boys,
        'most_disliked_by': most_disliked_by,
        'allowed_to_rate': allowed_to_rate,
    }

    return render(request, 'books/book_detail.html', context)
