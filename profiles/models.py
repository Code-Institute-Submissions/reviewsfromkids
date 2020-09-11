from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.forms import ModelForm


GENDER_CHOICES = [
    ('GIRL', 'girl'),
    ('BOY', 'boy'),
    ('UNKNOWN', 'prefer not to say'),
]


class UserProfile(models.Model):
    """
    User profile for tailoring reviews and queried results.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(null=True, blank=True, default=None,
                                     help_text="Format is year-month-day, e.g. 2010-12-26")
    hobbies = models.ManyToManyField('Hobby', blank=True)
    sports = models.ManyToManyField('Sport', blank=True)
    favorites = models.ManyToManyField('books.Book', blank=True)
    hobbies_known = models.BooleanField(default=False)
    sports_known = models.BooleanField(default=False)
    only_sports_known = models.BooleanField(default=False)
    only_hobbies_known = models.BooleanField(default=False)
    hobbies_and_sports_known = models.BooleanField(default=False)
    no_hobbies_and_sports_known = models.BooleanField(default=False)
    profile_complete = models.CharField(max_length=7, default='lvl-0')
    allowed_to_rate = models.BooleanField(default=False)
    age_in_years = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = UserProfile
        fields = [

            'first_name',
            'last_name',
            'gender',
            'date_of_birth',

            ]

        required = [

            'first_name',
            'last_name',
            'gender',
            'date_of_birth',

            ]


class Hobby(models.Model):

    class Meta:
        verbose_name_plural = 'Hobbies'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class UserProfileHobbyForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['hobbies']
        widgets = {
            'hobbies': forms.widgets.CheckboxSelectMultiple(),
        }


class Sport(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class UserProfileSportForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['sports']
        widgets = {
            'sports': forms.widgets.CheckboxSelectMultiple(),
        }
