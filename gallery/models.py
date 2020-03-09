from django.db import models

from event.models import Event
from users.models import User


class Gallery(models.Model):
    user = models.ForeignKey(User, related_name='gallery_images', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='gallery_events', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')
    is_approved = models.BooleanField(default=False)
