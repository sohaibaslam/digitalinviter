from django.db import models

from users.models import User
from themes.models import Theme
from digitalinviter.contants import Plans


class Event(models.Model):
    user = models.ForeignKey(User, related_name='user_events', on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, related_name='theme_events', on_delete=models.DO_NOTHING, null=True, default=None)
    plan = models.CharField(max_length=2, choices=Plans.choices, default=Plans.Basic)
    name = models.CharField(max_length=200)
    groom = models.CharField(max_length=100)
    bride = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=300)
    date = models.DateField()
    location = models.CharField(max_length=100)
    invite_description = models.CharField(max_length=1000)
    quote = models.CharField(max_length=2000)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.groom} and {self.bride} - Event No: {self.id}"


class EventTimeline(models.Model):
    event = models.ForeignKey(Event, related_name='event_timeline', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.TimeField()
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class EventHost(models.Model):
    event = models.ForeignKey(Event, related_name='event_hosts', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class ThemeImage(models.Model):
    event = models.ForeignKey(Event, related_name='theme_events', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='themes')
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.event} | {self.image_name} | {self.image.url}'


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('event', 'user')

    def __str__(self):
        return f'{self.event} | {self.user}'
