import django_filters
from django_filters import CharFilter, NumberFilter

from .models import *

class BookFilter(django_filters.FilterSet):

    start_age = NumberFilter(field_name='age', lookup_expr='gte')
    end_age = NumberFilter(field_name='age', lookup_expr='lte')
    
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'], 
            'author': ['icontains'], 
            'category': ['exact'], 
            # 'rating_all': ['exact'],
            'gender': ['icontains'],
        }


        # fields = ['title', 'author', 'category', 'rating_all']
