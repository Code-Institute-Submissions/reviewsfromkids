from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from profiles.models import UserProfile, Hobby, Sport
from django.core.exceptions import ValidationError



# Create your models here.
class Category(models.Model):

    class Meta: # 6.1
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

GENDER_CHOICES_POSITIVE = [
    ('not known yet', 'not known yet'),
    ('girls', 'girls'),
    ('boys', 'boys'),
    ('all, this most be really good!', 'all, this most be really good!'),
]

GENDER_CHOICES_NEGATIVE = [
    ('not known yet', 'not known yet'),
    ('girls', 'girls'),
    ('boys', 'boys'),
    ('all, this most be really bad...', 'all, this most be really bad...'),
]

class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    pages = models.IntegerField()
    tags = TaggableManager()
    age_on_book = models.CharField(max_length=254, null=True, blank=True)
    date_added = models.DateField(auto_now_add=False)
    featured_item = models.BooleanField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    number_of_ratings = models.IntegerField()
    boys_avg_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    boys_number_of_ratings = models.IntegerField()
    girls_avg_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    girls_number_of_ratings = models.IntegerField()
    most_liked_by = models.CharField(max_length=150, default='not known yet', choices=GENDER_CHOICES_POSITIVE)
    most_disliked_by = models.CharField(max_length=150, default='not known yet', choices=GENDER_CHOICES_NEGATIVE)
    recommended_age = models.CharField(max_length=254, default='not known yet')
    not_recommended_by_age = models.CharField(max_length=54, default='not known yet')
    star_rating_all = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    star_rating_boys = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    star_rating_girls = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    
    def __str__(self):
        return self.title


class Rating(models.Model):
    """ 
    Rating model.
    """
    rated_by = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    book_id = models.ForeignKey('Book', on_delete=models.PROTECT, related_name='book_id_of_rating')
    gender = models.CharField(max_length=25, null=True, blank=True)
    age_rating_years = models.IntegerField()
    age_rating_months = models.IntegerField()
    rating = models.IntegerField(null=True, blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    sports = models.ManyToManyField(Sport, blank=True)
    date_added = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.book_id.title
