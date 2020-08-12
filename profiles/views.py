from django.shortcuts import render, get_object_or_404
from .models import *
from books.models import Rating, Book

# Create your views here.
def profile(request):
    """ Display user profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    hobby = profile.hobbies.all().order_by('name')
    sport = profile.sports.all().order_by('name')

    ratings_high = Book.objects.filter(rating__rated_by=profile, rating__rating__gte=4)
    ratings_low = Book.objects.filter(rating__rated_by=profile, rating__rating__lte=2)
    ratings_ok = Book.objects.filter(rating__rated_by=profile, rating__rating=3)


    template = 'profiles/profile.html'
    context = {
        'hobby':hobby,
        'sport': sport,
        'profile': profile,
        'ratings_high': ratings_high,
        'ratings_low': ratings_low,
        'ratings_ok': ratings_ok,
        }

    return render(request, template, context)

def add_personal(request):
    """ User adds personal information to profile """

    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Grab POST values
    if request.POST:
        user = profile
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        print(profile.pk)

    # Store POST values in record
    UserProfile.objects.filter(id=profile.pk).update(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date_of_birth,
    )

    template = 'profiles/profile.html'
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'gender': gender,
        'date_of_birth': date_of_birth,
    }

    return render(request, template, context)

# def add_sport(request):
#     """ User can edit his/her hobbies """
    
#     sports = profile.sports.all().order_by('name')



