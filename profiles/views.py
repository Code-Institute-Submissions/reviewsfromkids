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