from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, When, Count

from digitalinviter.permissions import UserLevelPermission, EventLevelPermission
from rsvp.serializers import RSVPSerializer
from rsvp.models import RSVP


class RSVPViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    permission_classes = [UserLevelPermission]

    def create(self, request, *args, **kwargs):
        rsvp = RSVP.objects.filter(user=request.data['user'], event=request.data['event']).first()
        if rsvp:
            rsvp.is_attending = request.data.get('is_attending') == 'true'
            rsvp.save()
            return Response(RSVPSerializer(rsvp).data)

        return super().create(request, *args, **kwargs)

    @action(detail=True)
    def get_event_rsvp(self, request, pk=None):
        rsvp = self.get_queryset().filter(event=pk).values(
            'user__username', 'user__profile_url', 'is_attending').annotate(
            attending=Count(
                Case(
                    When(is_attending=True, then=1)
                )
            ),
            not_attending=Count(
                Case(
                    When(is_attending=False, then=1)
                )
            )
        )

        return Response(rsvp)
