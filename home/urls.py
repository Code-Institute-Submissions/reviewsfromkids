from django.contrib import admin
from django.urls import path
from . import views # 3.4

# 3.2 Paste the content from the project-level urls.py
urlpatterns = [
    path('', views.index, name='home'), # 3.3 Add an empty path to indicate this is the route URL
]