from django.db import models


class Event(models.Model):
    groom = models.CharField(max_length=100)
    bride = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=300)
    date = models.DateField()
    location = models.CharField(max_length=100)
    invite_description = models.CharField(max_length=1000)
    quote = models.CharField(max_length=2000)
    gmap_link = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.groom} and {self.bride}"


class EventTimeline(models.Model):
    event = models.ForeignKey(Event, related_name='event_timeline', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.TimeField()
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class EventHost(models.Model):
    event = models.ForeignKey(Event, related_name='event_hosts', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
