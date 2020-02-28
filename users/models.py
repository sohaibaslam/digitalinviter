from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=True)
    fb_profile_url = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
