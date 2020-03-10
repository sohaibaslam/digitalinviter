from django.db import models

from users.models import User
from event.models import Event


class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'event')
