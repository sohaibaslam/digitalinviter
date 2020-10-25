from django.db import models

from users.models import User
from event.models import Event


class GiftItem(models.Model):
    name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.event_id} | {self.name}'


class GiftBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registry = models.ForeignKey(GiftItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} | {self.registry.name}'
