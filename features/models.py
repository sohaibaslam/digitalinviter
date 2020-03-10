from django.contrib.postgres.fields import JSONField
from django.db import models

from digitalinviter.contants import Plans


class Feature(models.Model):
    plan = models.CharField(max_length=2, choices=Plans.choices, unique=True)
    features = JSONField()

    def __str__(self):
        return self.plan
