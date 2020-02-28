from django.contrib.postgres.fields import JSONField
from django.db import models

from users.models import User


class Theme(models.Model):
    name = models.CharField(max_length=100)
    configuration = JSONField(default=dict)

    def __str__(self):
        return self.name
