from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """ 
    User profile for tailoring reviews and queried results.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE) # try to anonymize ratings and votes for books
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    hobbies = models.ManyToManyField('Hobby', blank=True)
    sports = models.ManyToManyField('Sport', blank=True)
    
    
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

class Hobby(models.Model):

    class Meta: # 6.1
        verbose_name_plural = 'Hobbies'
    
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name