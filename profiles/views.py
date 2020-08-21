from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from books.models import Rating, Book
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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

@login_required
def book_finder_user(request):
    """
    Series of questions to find books that fit.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all()
    user_sport = profile.sports.all()

    # Check what personal profile information is available. User is known by default (pk).
    dobgender_available = False
    onlydob_available = False
    onlygender_available = False
    onlyuser_available = False
    
    if profile.date_of_birth == None:
        dob_available = False
    else:
        dob_available = True

    if profile.gender == "":
        gender_available = False
    else:
        gender_available = True
    
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True
    
    # Check hobbies and sports
    onlyhobby_available = False
    onlysport_available = False
    hobbysport_available = False
    no_hobbysport_available = False

    if user_hobby.exists()==True:
        hobby_available = True
    else:
        hobby_available = False

    if user_sport.exists()==True:
        sport_available = True
    else:
        sport_available = False

    if hobby_available == True and sport_available == True:
        hobbysport_available = True
    elif hobby_available == True and sport_available == False:
        onlyhobby_available = True
    elif hobby_available == False and sport_available == True:
        onlysport_available = True
    else:
        no_hobbysport_available = True

    context = {
        'profile': profile,
        'dobgender_available': dobgender_available,
        'onlydob_available': onlydob_available,
        'onlygender_available': onlygender_available,
        'onlyuser_available': onlyuser_available,
        'hobbysport_available': hobbysport_available,
        'onlyhobby_available': onlyhobby_available,
        'onlysport_available': onlysport_available,
        'no_hobbysport_available': no_hobbysport_available,

    }

    return render(request, 'profiles/book_finder_user.html', context)

@login_required
def book_finder_user_1(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    # Check what profile information is available. User is known by default (pk).
    dobgender_available = False
    onlydob_available = False
    onlygender_available = False
    onlyuser_available = False

    if profile.date_of_birth == None:
        dob_available = False
    else:
        dob_available = True

    if profile.gender == "":
        gender_available = False
    else:
        gender_available = True
    
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True
    
    # Grab form data
    if request.method == "POST":
        form = UserProfileForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_finder_user_2')

    context = {
        'profile': profile,
        'dobgender_available': dobgender_available,
        'onlydob_available': onlydob_available,
        'onlygender_available': onlygender_available,
        'onlyuser_available': onlyuser_available,
        'form': form,
    }

    return render(request, 'profiles/book_finder_user_1.html', context)

@login_required
def book_finder_user_2(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')

    # Check what profile information is available. User is known by default (pk).
    dobgender_available = False
    onlydob_available = False
    onlygender_available = False
    onlyuser_available = False

    if profile.date_of_birth == None:
        dob_available = False
    else:
        dob_available = True

    if profile.gender == "":
        gender_available = False
    else:
        gender_available = True
    
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True

    # Check hobbies and sports
    onlyhobby_available = False
    onlysport_available = False
    hobbysport_available = False
    no_hobbysport_available = False

    if user_hobby.exists()==True:
        hobby_available = True
    else:
        hobby_available = False

    if user_sport.exists()==True:
        sport_available = True
    else:
        sport_available = False

    if hobby_available == True and sport_available == True:
        hobbysport_available = True
    elif hobby_available == True and sport_available == False:
        onlyhobby_available = True
    elif hobby_available == False and sport_available == True:
        onlysport_available = True
    else:
        no_hobbysport_available = True
    
    form_hobby = UserProfileHobbyForm(instance=profile)
    form_sport = UserProfileSportForm(instance=profile)

    # Grab data from form
    if request.method == "POST":
        if request.POST.get('type_of_action')=='onlyhobby_available':
            form = UserProfileSportForm(instance=profile, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_finder_user_4')

        if request.POST.get('type_of_action')=='onlysport_available':
            form = UserProfileHobbyForm(instance=profile, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_finder_user_4')
        
        if request.POST.get('type_of_action')=='no_hobbysport_available':
            form = UserProfileHobbyForm(instance=profile, data = request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_finder_user_3')
        
    context = {
        'profile': profile,
        'user_hobby': user_hobby,
        'user_sport': user_sport,
        'dobgender_available': dobgender_available,
        'onlydob_available': onlydob_available,
        'onlygender_available': onlygender_available,
        'onlyuser_available': onlyuser_available,
        'form_hobby': form_hobby,
        'form_sport': form_sport,
        'onlyhobby_available': onlyhobby_available,
        'onlysport_available': onlysport_available,
        'no_hobbysport_available': no_hobbysport_available,
    }

    return render(request, 'profiles/book_finder_user_2.html', context)

@login_required
def book_finder_user_3(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')

    # Check what profile information is available. User is known by default (pk).
    dobgender_available = False
    onlydob_available = False
    onlygender_available = False
    onlyuser_available = False

    if profile.date_of_birth == None:
        dob_available = False
    else:
        dob_available = True

    if profile.gender == "":
        gender_available = False
    else:
        gender_available = True
    
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True

    form_sport = UserProfileSportForm(instance=profile)

    if request.method == "POST":
        form = UserProfileSportForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_finder_user_4')
    
    context = {
        'profile': profile,
        'user_hobby': user_hobby,
        'user_sport': user_sport,
        'dobgender_available': dobgender_available,
        'onlydob_available': onlydob_available,
        'onlygender_available': onlygender_available,
        'onlyuser_available': onlyuser_available,
        'form_sport': form_sport,
    }

    return render(request, 'profiles/book_finder_user_3.html', context)


@login_required
def book_finder_user_4(request):
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
    
    return render(request, 'profiles/book_finder_user_4.html', context)