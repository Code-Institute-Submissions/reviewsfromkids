import os

import stripe

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def donations(request):
    return render(request, 'donations/donations.html')


def success(request):
    return render(request, 'donations/success.html')

# For future reference:
# if os.path.exists("env.py"):
#     from env import STRIPE_API_KEY_TEST
#     stripe.api_key = STRIPE_API_KEY_TEST
# else:
#     stripe.api_key = os.environ.get('STRIPE_API_KEY_TEST')