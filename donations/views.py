from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

import os
from env import STRIPE_API_KEY_TEST

# Create your views here.

stripe.api_key = STRIPE_API_KEY_TEST

def donations(request):
    return render(request, 'donations/donations.html')


def charge(request):
     
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])
        
        customer = stripe.Customer.create(
            name = request.POST['name'],
            email = request.POST['email'],
            source = request.POST['stripeToken'],
        )

        if request.POST.get('description') == '':
                description='Donation'
        else:
            description = request.POST.get('description')

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'eur',
            description = description,
            
        )

    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'donations/success.html', {'amount':amount})