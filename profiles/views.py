from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from books.models import Rating, Book
from django.http import HttpResponseRedirect


# Create your views here.
def profile(request):
    """ Display user profile """

    hobby=Hobby.objects.all()
    sport=Sport.objects.all()

    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')

    ratings_high = Book.objects.filter(rating__rated_by=profile, rating__rating__gte=4)
    ratings_low = Book.objects.filter(rating__rated_by=profile, rating__rating__lte=2)
    ratings_ok = Book.objects.filter(rating__rated_by=profile, rating__rating=3)


    template = 'profiles/profile.html'
    context = {
        'hobby': hobby,
        'sport': sport,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        'ratings_high': ratings_high,
        'ratings_low': ratings_low,
        'ratings_ok': ratings_ok,
        }

    if hobby:
        print(hobby)
        print(hobby.values())
    else:
        print('no hobbies selected')

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

    # Store POST values in record
    UserProfile.objects.filter(id=profile.pk).update(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        date_of_birth=date_of_birth,
    )

    next = request.POST.get('next', 'profile')
    return HttpResponseRedirect(next)

def add_hobby(request):
    """ User can add his/her hobbies """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Grab POST values
    if request.POST:
        user = profile
        userhobby = request.POST.get('userhobby')
        print(userhobby)
    
    # UserProfile.objects.filter(id=profile.pk).update(
    #     hobbies=userhobby,
    # )

    next = request.POST.get('next', 'profile')
    return HttpResponseRedirect(next)


