from django.db import transaction
from django.db.models import F
from django.shortcuts import render
from rest_framework import status
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
        event = Event.objects.get(id=request.data['event_id'])
        event_timeline = request.data.pop('event_timeline', [])
        event_hosts = request.data.pop('event_hosts', [])

        for timeline in event_timeline or []:
            timeline_id = timeline.get('id')
            timeline['event'] = event if timeline_id else request.data["event_id"]

            if timeline_id:
                instance = EventTimeline.objects.get(id=timeline_id)
                EventTimelineSerializer(instance).update(instance, timeline)
            else:
                timeline_serializer = EventTimelineSerializer(data=timeline)
                if timeline_serializer.is_valid(raise_exception=True):
                    timeline_serializer.save()

        for host in event_hosts or []:
            host_id = host.get('id')
            host['event'] = event if host_id else request.data["event_id"]

            if host_id:
                instance = EventHost.objects.get(id=host['id'])
                EventHostSerializer().update(instance, host)
            else:
                host_serializer = EventHostSerializer(data=host)
                if host_serializer.is_valid(raise_exception=True):
                    host_serializer.save()

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

    def create(self, request, *args, **kwargs):
        if Invitation.objects.filter(user=request.data["user"], event=request.data["event"]):
            return Response(status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def get_my_invitations(self, request, *args, **kwargs):
        return Response(self.get_queryset().filter(user=request.user).values(
            'event__id', 'event__name').annotate(template=F('event__theme__name')))


def privacy_policy(request, *args, **kwargs):
    return render(request, 'event/privacy_policy.html')
