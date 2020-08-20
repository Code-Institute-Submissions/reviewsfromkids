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
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class List(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


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
    age = models.IntegerField()
    gender = models.CharField(max_length=25)
    number_of_ratings = models.IntegerField()
    # part_of_lists = models.ManyToManyField('List', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField(auto_now_add=False)
    featured_item = models.BooleanField()
    
    def __str__(self):
        return self.title


class Rating(models.Model):
    """ 
    Rating model.
    """
    rated_by = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    # rated_by = models.OneToOneField(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey('Book', on_delete=models.PROTECT)
    gender = models.CharField(max_length=25, null=True, blank=True)
    age_rating_years = models.IntegerField()
    age_rating_months = models.IntegerField()
    rating = models.IntegerField(null=True, blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    sports = models.ManyToManyField(Sport, blank=True)
    
    def __str__(self):
        return self.book_id.title
