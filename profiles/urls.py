from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_personal', views.edit_personal, name='edit_personal'),
    path('edit_hobby', views.edit_hobby, name='edit_hobby'),
    path('edit_sport', views.edit_sport, name='edit_sport'),
    path('book_finder_user', views.book_finder_user,  name='book_finder_user'),
]