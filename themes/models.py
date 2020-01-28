from django.contrib.postgres.fields import JSONField
from django.db import models

from users.models import User


class Theme(models.Model):
    name = models.CharField(max_length=100)
    configuration = JSONField(default=dict)

    def __str__(self):
        return self.name


class ThemeImage(models.Model):
    user = models.ForeignKey(User, related_name='theme_images', on_delete=models.CASCADE)
    image = models.ImageField()
