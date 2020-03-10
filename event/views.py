from django.db import transaction
from django.db.models import F
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from event.models import Event, EventTimeline, EventHost, ThemeImage, Invitation
from themes.models import Theme
from event.serializers import (EventSerializer, EventTimelineSerializer, EventHostSerializer,
                               ThemeImageSerializer, InvitationSerializer)
from digitalinviter.permissions import UserLevelPermission, EventLevelPermission


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [UserLevelPermission]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        event = Event.objects.get(id=response.data['id'])

        event_timeline = request.data.get('event_timeline')
        event_hosts = request.data.get('event_hosts')

        EventTimeline.objects.bulk_create([EventTimeline(event=event, **timeline) for timeline in event_timeline or []])
        EventHost.objects.bulk_create([EventHost(event=event, **host) for host in event_hosts or []])

        return response

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        event_timeline = request.data.get('event_timeline')
        event_hosts = request.data.get('event_hosts')

        for timeline in event_timeline or []:
            instance = EventTimeline.objects.get(id=timeline['id'])
            timeline['event'] = instance.event
            EventTimelineSerializer(instance).update(instance, timeline)

        for host in event_hosts or []:
            instance = EventHost.objects.get(id=host['id'])
            host['event'] = instance.event
            EventHostSerializer().update(instance, host)

        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        theme_images = Theme.objects.get(id=response.data['theme']).configuration['images']
        event_theme_images = ThemeImage.objects.filter(image_name__in=theme_images, event=response.data['id'])

        config = {'theme_images': {image.image_name: image.image.url for image in event_theme_images}}
        response.data['config'] = config.copy()
        response.data['is_owner'] = response.data['user'] == request.user.id

        return response

    @action(detail=False)
    def get_my_events(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(self.get_queryset().filter(
                user=request.user).values('name', 'id').annotate(template=F('theme__name')))

        return Response([])


class EventTimelineViewSet(ModelViewSet):
    queryset = EventTimeline.objects.all()
    serializer_class = EventTimelineSerializer


class EventHostViewSet(ModelViewSet):
    queryset = EventHost.objects.all()
    serializer_class = EventHostSerializer


class ThemeImageViewSet(ModelViewSet):
    serializer_class = ThemeImageSerializer
    queryset = ThemeImage.objects.all()
    permission_classes = [UserLevelPermission, EventLevelPermission]


class InvitationViewSet(ModelViewSet):
    serializer_class = InvitationSerializer
    queryset = Invitation.objects.all()
    permission_classes = [UserLevelPermission]

    @action(methods=['GET'], detail=False)
    def get_my_invitations(self, request, *args, **kwargs):
        return Response(self.get_queryset().filter(user=request.user).values(
            'event__id', 'event__name').annotate(template=F('event__theme__name')))


def privacy_policy(request, *args, **kwargs):
    return render(request, 'event/privacy_policy.html')
