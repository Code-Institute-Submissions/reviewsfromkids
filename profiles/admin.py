from django.contrib import admin
from .models import UserProfile, Hobby, Sport

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Hobby)
admin.site.register(Sport)