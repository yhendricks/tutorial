from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    website = models.URLField(default='')
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    #company = models.ForeignKey(Company, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    london = UserProfileManager()

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

