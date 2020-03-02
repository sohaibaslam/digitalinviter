from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up


class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=True)
    profile_url = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


@receiver(user_signed_up)
def save_profile_url(user, **kwargs):
    avatar_url = None
    social_login = kwargs.get('sociallogin')

    if social_login:
        if social_login.account.provider == 'facebook':
            avatar_url = f"https://graph.facebook.com/{social_login.account.extra_data.get('id', '')}/picture"

    if avatar_url:
        user.profile_url = avatar_url

    user.save()
