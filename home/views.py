from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from profiles.models import UserProfile
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def index(request):
    """ A view to return the index page """
    books = Book.objects.all()
    featured_books = Book.objects.filter(featured_item = True)
    recent_books = Book.objects.filter(date_added = "2020-07-16")
    
    user=request.user
    userprofile=None
    user_logged_in=False

    # Check if user is logged in
    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_logged_in=True

    context = {
        'featured_books': featured_books,
        'recent_books': recent_books,
        'user_logged_in': user_logged_in,
        'profile': userprofile,
    }

    return render(request, 'home/index.html', context)


# Create your views here.
def contact(request):
    """ A view to render the contact page """
    cc_myself = False
    
    if request.method == 'GET':
        form = ContactForm()

    else: 
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            copy_to_myself = form.cleaned_data['copy_to_myself']

            recipients = ['info@reviewsfromkids.com']

            if cc_myself:
                recipients.append(sender)

            send_mail(name, message, email, recipients)

            messages.info(request, f'Mail sent successfully, thank you')

            return redirect('contact')

    context = {
        'form': form,
    }

    return render(request, 'home/contact.html', context)

def about(request):
    """ A view to render the about page """
    
    user=request.user
    userprofile=None
    user_logged_in=False

    # Check if user is logged in
    if user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        user_logged_in=True

    context = {

        'user_logged_in': user_logged_in,
        'profile': userprofile,
    }

    return render(request, 'home/about.html', context)

