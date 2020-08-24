import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *

class BookFilter(django_filters.FilterSet):

    start_rating = NumberFilter(field_name='avg_rating', lookup_expr='gte')
    
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'], 
            'author': ['icontains'], 
            'category': ['exact'], 
            'gender': ['icontains'],
        }