from django.db import models

from event.models import Event
from users.models import User


class Greeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} | {self.event}'
