from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_personal', views.edit_personal, name='edit_personal'),
    path('edit_hobby', views.edit_hobby, name='edit_hobby'),
    path('edit_sport', views.edit_sport, name='edit_sport'),
    path('book_finder_edit_hobby', views.book_finder_edit_hobby, name='book_finder_edit_hobby'),
    path('book_finder_edit_sport', views.book_finder_edit_sport, name='book_finder_edit_sport'),
    path('book_finder_user', views.book_finder_user,  name='book_finder_user'),
    path('book_finder_user_1', views.book_finder_user_1,  name='book_finder_user_1'),
    path('book_finder_user_2', views.book_finder_user_2,  name='book_finder_user_2'),
    path('book_finder_user_3', views.book_finder_user_3,  name='book_finder_user_3'),
    path('book_finder_user_4', views.book_finder_user_4,  name='book_finder_user_4'),
    path('book_finder_user_5', views.book_finder_user_5,  name='book_finder_user_5'),
]