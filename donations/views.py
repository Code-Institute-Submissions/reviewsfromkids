from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

import os

# if os.path.exists("env.py"):
#     from env import STRIPE_API_KEY_TEST
#     stripe.api_key = STRIPE_API_KEY_TEST
# else:
#     stripe.api_key = os.environ.get('STRIPE_API_KEY_TEST')


def donations(request):
    return render(request, 'donations/donations.html')


def success(request):
    return render(request, 'donations/success.html')