from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_personal', views.add_personal, name='add_personal'),
    path('add_hobby', views.add_hobby, name='add_hobby')
]