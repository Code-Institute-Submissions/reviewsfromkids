from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from books.models import Rating, Book, Category
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO
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
            
            profile.save()

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

            profile.save()

            return redirect('book_finder_user_5')

    # Load edit sport page
    template = 'profiles/book_finder_edit_sport.html'
    context = {'form': form}
    return render(request, template, context)


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
    Series of questions to find books that fit.
    First check if profile is complete. If so, redirect to last step.
    If not complete profile over the next steps.
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
    
    form_hobby = UserProfileHobbyForm(instance=profile)
    form_sport = UserProfileSportForm(instance=profile)

    # Grab data from form
    if request.method == "POST":
        if request.POST.get('type_of_action')=='onlyhobby_available':
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

                profile.save()

                return redirect('book_finder_user_4')

        if request.POST.get('type_of_action')=='onlysport_available':
            form = UserProfileHobbyForm(instance=profile, data = request.POST)
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

                profile.save()

                return redirect('book_finder_user_4')
        
        if request.POST.get('type_of_action')=='no_hobbysport_available':
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
                
                profile.save()

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

            profile.save()
            
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

    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')
    categories = Category.objects.all()

    # Build query
    #Find positive ratings 4 and 5 for age and gender user
    user_dob = profile.date_of_birth
    date_calc = datetime.now()
    age_rating = relativedelta(date_calc, user_dob)
    age_rating_years = age_rating.years
    age_rating_months = age_rating.months  
    
    ratings_high = Rating.objects.filter(rating__gte=4, age_rating_years=age_rating_years, gender=profile.gender)

    # Find book objects for the high rates that match users' age and gender
    book_ids = ratings_high.values('book_id_id')
    books = Book.objects.filter(pk__in=book_ids)
    
    """
    Need to remove books that user has rated himself/herself from recommendations
    """
    # Find books that match users' hobbies
    # all_hobbies_of_positive_ratings = Hobby.objects.filter(rating__book_id=book_id, rating__rating__gte=4)
    # hobbies_positive_ratings = all_hobbies_of_positive_ratings.values('name').annotate(Count('name')).order_by('-name__count')[:2]

    # <QuerySet [{'name': 'dancing', 'name__count': 1}, {'name': 'lego', 'name__count': 1}]>
    testset1 = Book.objects.filter(pk__in=book_ids)
    testset2 = Book.objects.filter(pk__in=book_ids)
    print(type(testset1))
    print(testset1)
    testset1_names = testset1.values_list('author')
    testset2_names = testset2.values_list('author')
    print(testset1_names)
    print(type(testset1_names))
    # testset1_names = testset2.values_list('name')
    key1 = frozenset(testset1_names)
    key2 = frozenset(testset2_names)
 
    common_items = frozenset.intersection(key1, key2)
    print(common_items)
    


    context = {
        'user': user,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        'categories': categories,
        'ratings_high': ratings_high,
        'books': books,
        'common_items': common_items,
        }
    
    return render(request, 'profiles/book_finder_user_4.html', context)


@login_required
def book_finder_user_5(request):
    """ Display user profile """

    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_hobby = profile.hobbies.all().order_by('name')
    user_sport = profile.sports.all().order_by('name')
    
    context = {
        'user': user,
        'user_hobby':user_hobby,
        'user_sport': user_sport,
        'profile': profile,
        }
    
    return render(request, 'profiles/book_finder_user_5.html', context)

