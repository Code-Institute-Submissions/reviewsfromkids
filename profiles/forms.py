from django import forms
from django.forms import ModelForm

from .models import UserProfile

# class UserProfileForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = [
#             'first_name', 
#             'last_name', 
#             'gender', 
#             'date_of_birth', 
#             # 'hobbies', 
#             # 'sports'
#             ]