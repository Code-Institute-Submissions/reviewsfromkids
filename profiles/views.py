from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from books.models import Rating, Book, Category
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO
from django.contrib import messages
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

    a = Rating.objects.filter(rated_by=profile, rating__gte=4)
    b = a.values('book_id_id')
    ratings_high = Book.objects.filter(pk__in=b)

    c = Rating.objects.filter(rated_by=profile, rating=3)
    d = c.values('book_id_id')
    ratings_ok = Book.objects.filter(pk__in=d)

    e = Rating.objects.filter(rated_by=profile, rating__lte=2)
    f = e.values('book_id_id')
    ratings_low = Book.objects.filter(pk__in=f)
    
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
        # 'no_ratings': no_ratings,
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
            
            # Update profile complete lvl
            user_hobby = profile.hobbies.all()
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()
            
            messages.success(request, f'Profile updated, thank you')

            return redirect('profile')

    # Load edit personal page
    template = 'profiles/edit_personal.html'
    context = {'form': form}
    return render(request, template, context)


def edit_hobby(request):
    """ User can add his/her hobbies """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all()

    # Render existing data on form
    form = UserProfileHobbyForm(instance=profile)

    if request.method == "POST":
        form = UserProfileHobbyForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()
            
            # Set bools needed for bookfinder functionality
            if profile.hobbies.all().exists()==True:
                profile.hobbies_known = True
            else:
                profile.hobbies_known = False
            
            if profile.hobbies_known == True and profile.sports_known == True:
                profile.hobbies_and_sports_known = True
            else:
                profile.hobbies_and_sports_known = False

            if profile.hobbies_known == True and profile.sports_known == False:
                profile.only_hobbies_known = True
            else:
                profile.only_hobbies_known = False

            if profile.hobbies_known == False and profile.sports_known == True:
                profile.only_sports_known = True
            else:
                profile.only_sports_known = False

            if profile.hobbies_known == False and profile.sports_known == False:
                profile.no_hobbies_and_sports_known = True
            else:
                profile.no_hobbies_and_sports_known = False
            
            # Update profile complete lvl
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()

            messages.success(request, f'Hobbies updated, thank you')

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

            # Set bools needed for bookfinder functionality
            if profile.sports.all().exists()==True:
                profile.sports_known = True
            else:
                profile.sports_known = False
            
            if profile.hobbies_known == True and profile.sports_known == True:
                profile.hobbies_and_sports_known = True
            else:
                profile.hobbies_and_sports_known = False

            if profile.hobbies_known == True and profile.sports_known == False:
                profile.only_hobbies_known = True
            else:
                profile.only_hobbies_known = False

            if profile.hobbies_known == False and profile.sports_known == True:
                profile.only_sports_known = True
            else:
                profile.only_sports_known = False

            if profile.hobbies_known == False and profile.sports_known == False:
                profile.no_hobbies_and_sports_known = True
            else:
                profile.no_hobbies_and_sports_known = False

            # Update profile complete lvl
            user_hobby = profile.hobbies.all()
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()

            messages.success(request, f'Sports updated, thank you')
            profile.save()
            
            return redirect('profile')

    # Load edit sport page
    template = 'profiles/edit_sport.html'
    context = {'form': form}
    return render(request, template, context)


def book_finder_edit_hobby(request):
    """ User can add his/her hobbies """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Render existing data on form
    form = UserProfileHobbyForm(instance=profile)

    if request.method == "POST":
        form = UserProfileHobbyForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()

            # Set bools needed for bookfinder functionality
            if profile.hobbies.all().exists()==True:
                profile.hobbies_known = True
            else:
                profile.hobbies_known = False
            
            if profile.hobbies_known == True and profile.sports_known == True:
                profile.hobbies_and_sports_known = True
            else:
                profile.hobbies_and_sports_known = False

            if profile.hobbies_known == True and profile.sports_known == False:
                profile.only_hobbies_known = True
            else:
                profile.only_hobbies_known = False

            if profile.hobbies_known == False and profile.sports_known == True:
                profile.only_sports_known = True
            else:
                profile.only_sports_known = False

            if profile.hobbies_known == False and profile.sports_known == False:
                profile.no_hobbies_and_sports_known = True
            else:
                profile.no_hobbies_and_sports_known = False
            
            # Update profile complete lvl
            user_hobby = profile.hobbies.all()
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()
            
            messages.success(request, f'Hobbies updated, thank you')

            profile.save()

            return redirect('book_finder_user_5')

    # Load edit hobby page
    template = 'profiles/book_finder_edit_hobby.html'
    context = {'form': form}
    return render(request, template, context)


def book_finder_edit_sport(request):
    """ User can add his/her sports """
    
    # Get userprofile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Render existing data on form
    form = UserProfileSportForm(instance=profile)

    if request.method == "POST":
        form = UserProfileSportForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()

            # Set bools needed for bookfinder functionality
            if profile.sports.all().exists()==True:
                profile.sports_known = True
            else:
                profile.sports_known = False
            
            if profile.hobbies_known == True and profile.sports_known == True:
                profile.hobbies_and_sports_known = True
            else:
                profile.hobbies_and_sports_known = False

            if profile.hobbies_known == True and profile.sports_known == False:
                profile.only_hobbies_known = True
            else:
                profile.only_hobbies_known = False

            if profile.hobbies_known == False and profile.sports_known == True:
                profile.only_sports_known = True
            else:
                profile.only_sports_known = False

            if profile.hobbies_known == False and profile.sports_known == False:
                profile.no_hobbies_and_sports_known = True
            else:
                profile.no_hobbies_and_sports_known = False
            
            # Update profile complete lvl
            user_hobby = profile.hobbies.all()
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()
            
            messages.success(request, f'Sports updated, thank you')

            profile.save()

            return redirect('book_finder_user_5')

    # Load edit sport page
    template = 'profiles/book_finder_edit_sport.html'
    context = {'form': form}
    return render(request, template, context)


def book_finder(request):
    """
    Series of questions to find books that fit.
    Non logged in user will first be checked: has account or not?
    If account: redirect to book_finder_user, which has @login_required.
    If no account: stimulate to create one.
    After that, user can start flow for book_finder_user.
    """
    context = {}

    return render(request, 'profiles/book_finder.html', context)


@login_required
def book_finder_user(request):
    """
    Series of questions to find books that fit.
    First check if profile is complete. If so, redirect to last step.
    If not complete profile over the next steps.
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

    if profile.gender == None:
        gender_available = False
    else:
        gender_available = True
    
    # Pass results to template
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True
    
    context = {
        'profile': profile,
        'dobgender_available': dobgender_available,
        'onlydob_available': onlydob_available,
        'onlygender_available': onlygender_available,
        'onlyuser_available': onlyuser_available,
    }
    
    return render(request, 'profiles/book_finder_user.html', context)


@login_required
def book_finder_user_1(request):
    """
    Complete profile information.
    Information that is known is preloaded.
    """
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
    
    # Pass results to template
    if dob_available == True and gender_available == True:
        dobgender_available = True
    elif dob_available == True and gender_available == False:
        onlydob_available = True
    elif dob_available == False and gender_available == True:
        onlygender_available = True
    else:
        onlyuser_available = True
    
    # Grab form data and save
    if request.method == "POST":
        form = UserProfileForm(instance=profile, data = request.POST)
        if form.is_valid():
            form.save()

            # Update profile complete lvl
            user_hobby = profile.hobbies.all()
            user_sport = profile.sports.all()

            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()
            
            messages.success(request, f'Profile updated, thank you')

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
    """
    If user has no hobbies and no sports: start with hobbies and then in book_finder_user_3 add sports.
    If user has only sports: add hobbies.
    If user has only hobbies: add sports.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')
    no_hobbysport_available = None

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
    
    form_hobby = UserProfileHobbyForm(instance=profile)
    form_sport = UserProfileSportForm(instance=profile)

    # Grab data from form
    if request.method == "POST":
        if request.POST.get('type_of_action')=='onlyhobby_available':
            form = UserProfileSportForm(instance=profile, data = request.POST)
        
        if request.POST.get('type_of_action')=='onlysport_available':
            form = UserProfileHobbyForm(instance=profile, data = request.POST)
            
        if request.POST.get('type_of_action')=='no_hobbysport_available':
            form = UserProfileHobbyForm(instance=profile, data = request.POST)
            no_hobbysport_available = True
            
        if form.is_valid():
            form.save()

        # Set bools needed for bookfinder functionality
        if profile.sports.all().exists()==True:
            profile.sports_known = True
        else:
            profile.sports_known = False

        if profile.hobbies.all().exists()==True:
            profile.hobbies_known = True
        else:
            profile.hobbies_known = False

        if profile.hobbies_known == True and profile.sports_known == True:
            profile.hobbies_and_sports_known = True
        else:
            profile.hobbies_and_sports_known = False

        if profile.hobbies_known == True and profile.sports_known == False:
            profile.only_hobbies_known = True
        else:
            profile.only_hobbies_known = False

        if profile.hobbies_known == False and profile.sports_known == True:
            profile.only_sports_known = True
        else:
            profile.only_sports_known = False

        if profile.hobbies_known == False and profile.sports_known == False:
            profile.no_hobbies_and_sports_known = True
        else:
            profile.no_hobbies_and_sports_known = False

        # Update profile complete lvl
        if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
            profile.profile_complete = "lvl-1"
    
        if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
            profile.profile_complete = "lvl-2"

        if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
            profile.profile_complete = "lvl-3"

        profile.save()
        
        messages.success(request, f'Profile updated, thank you')
        

        if  no_hobbysport_available == True:
            return redirect('book_finder_user_3')
        else:
            return redirect('book_finder_user_4')
    
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
    }

    return render(request, 'profiles/book_finder_user_2.html', context)

@login_required
def book_finder_user_3(request):
    """
    Only for user that has no hobbies and no sports.
    In previous step (book_finder_user_2) the hobbies are completed.
    In this step the sports are handled.
    """

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

            # Set bools needed for bookfinder functionality
            if profile.sports.all().exists()==True:
                profile.sports_known = True
            else:
                profile.sports_known = False
            
            if profile.hobbies_known == True and profile.sports_known == True:
                profile.hobbies_and_sports_known = True
            else:
                profile.hobbies_and_sports_known = False

            if profile.hobbies_known == True and profile.sports_known == False:
                profile.only_hobbies_known = True
            else:
                profile.only_hobbies_known = False

            if profile.hobbies_known == False and profile.sports_known == True:
                profile.only_sports_known = True
            else:
                profile.only_sports_known = False

            if profile.hobbies_known == False and profile.sports_known == False:
                profile.no_hobbies_and_sports_known = True
            else:
                profile.no_hobbies_and_sports_known = False

            # Update profile complete lvl
            if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
                profile.profile_complete = "lvl-1"
        
            if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
                profile.profile_complete = "lvl-2"

            if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
                profile.profile_complete = "lvl-3"

            profile.save()
            
            messages.success(request, f'Profile updated, thank you')

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
    """ 
    Books that fit your profile! Based on age, gender, hobbies, sports and your own ratings.
    """

    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')
    categories = Category.objects.all()
    user_dob = profile.date_of_birth
    date_calc = datetime.now()
    age_rating = relativedelta(date_calc, user_dob)
    age_rating_years = age_rating.years
    
    # Collect users' hobbies and find ratings with the same hobbies. Then filter on high rating and users' gender and age 
    hobby_ids = user_hobby.values('id')
    a = Rating.objects.filter(hobbies__in=hobby_ids, gender=profile.gender, rating__gte=4, age_rating_years=age_rating_years)
    b = a.values('book_id_id')

    # Same for sports
    sport_ids = user_sport.values('id')
    c = Rating.objects.filter(hobbies__in=sport_ids, gender=profile.gender, rating__gte=4, age_rating_years=age_rating_years)
    d = c.values('book_id_id')

    # Grab user's own ratings to remove from recommendation, take both positive and negative ratings
    e = Rating.objects.filter(rated_by=profile).exclude(rating=3)
    f = e.values('book_id_id')
   
    # Convert QuerySet Rating to QuerySet Book to show in template
    books = Book.objects.filter(pk__in=[b, d]).exclude(pk__in=f).distinct()

    context = {
        'user': user,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        'categories': categories,
        'age_rating_years': age_rating_years,
        'books': books,
        }
    
    return render(request, 'profiles/book_finder_user_4.html', context)


@login_required
def book_finder_user_5(request):
    """ 
    Special view for user to edit hobbies and sports. Redirects to book_finder_user_4.
    """

    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')

    # Update profile complete lvl
    if profile.first_name and profile.last_name and profile.date_of_birth and profile.gender:
        profile.profile_complete = "lvl-1"

    if profile.profile_complete == "lvl-1" and user_hobby.exists()==True or user_sport.exists()==True:
        profile.profile_complete = "lvl-2"

    if profile.profile_complete == "lvl-2" and user_hobby.exists()==True and user_sport.exists()==True:
        profile.profile_complete = "lvl-3"

    profile.save()
    
    context = {
        'user': user,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        }
    
    return render(request, 'profiles/book_finder_user_5.html', context)

