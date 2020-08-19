from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from books.models import Rating, Book
from django.http import HttpResponseRedirect
# from .forms import *


# Create your views here.
def profile(request):
    """ Display user profile """

    hobby=Hobby.objects.all()
    sport=Sport.objects.all()
    user = get_object_or_404(User, username=request.user)

    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')
    favorites = profile.favorites.all()

    ratings_high = Book.objects.filter(rating__rated_by=profile, rating__rating__gte=4)
    ratings_low = Book.objects.filter(rating__rated_by=profile, rating__rating__lte=2)
    ratings_ok = Book.objects.filter(rating__rated_by=profile, rating__rating=3)


    template = 'profiles/profile.html'

    context = {
        'user': user,
        'hobby': hobby,
        'sport': sport,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        'ratings_high': ratings_high,
        'ratings_low': ratings_low,
        'ratings_ok': ratings_ok,
        'favorites': favorites,
        }

    return render(request, template, context)

#Form with ModelForm
def edit_personal(request):

    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Render existing data in form
    form = UserProfileForm(instance=profile)

    # Check if form is updated via submit button i.e. POST
    if request.method == "POST":
        
        form = UserProfileForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    # Load edit personal page
    template = 'profiles/edit_personal.html'
    context = {'form': form}
    return render(request, template, context)


def edit_hobby(request):
    """ User can add his/her hobbies """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Render existing data on form
    form = UserProfileHobbyForm(instance=profile)

    if request.method == "POST":
        form = UserProfileHobbyForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    # Load edit hobby page
    template = 'profiles/edit_hobby.html'
    context = {'form': form}
    return render(request, template, context)


def edit_sport(request):
    """ User can add his/her sports """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Render existing data on form
    form = UserProfileSportForm(instance=profile)

    if request.method == "POST":
        form = UserProfileSportForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    # Load edit hobby page
    template = 'profiles/edit_sport.html'
    context = {'form': form}
    return render(request, template, context)