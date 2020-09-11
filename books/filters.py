import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *


class BookFilter(django_filters.FilterSet):

    rating = NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Book
        fields = {

            'title': ['icontains'],
            'author': ['icontains'],
            'category': ['exact'],
            'most_liked_by': ['exact'],
            'recommended_age': ['icontains']

        }
