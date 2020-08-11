from django.shortcuts import render, get_object_or_404
from .models import *
from books.models import Rating

# Create your views here.
def profile(request):
    """ Display user profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    hobby = profile.hobbies.all().order_by('name')
    sport = profile.sports.all().order_by('name')

    ratings = Rating.objects.filter(rated_by=profile)
    print(ratings)

    template = 'profiles/profile.html'
    context = {
        'hobby':hobby,
        'sport': sport,
        'profile': profile,
        'ratings': ratings,
        }

    return render(request, template, context)