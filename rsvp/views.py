from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from rsvp.serializers import RSVPSerializer
from rsvp.models import RSVP


class RSVPViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
