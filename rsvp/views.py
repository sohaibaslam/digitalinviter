from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from digitalinviter.permissions import UserLevelPermission, EventLevelPermission
from rsvp.serializers import RSVPSerializer
from rsvp.models import RSVP


class RSVPViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    permission_classes = [UserLevelPermission, EventLevelPermission]
