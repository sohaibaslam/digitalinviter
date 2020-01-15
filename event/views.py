from rest_framework.viewsets import ModelViewSet


from event.serializers import EventSerializer, EventTimelineSerializer, EventHostSerializer
from event.models import Event, EventTimeline, EventHost


class EventViewSet(ModelViewSet):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        event = super().create(request, *args, **kwargs)
        event_timeline = request.data.get('event_timeline')
        event_hosts = request.data.get('event_hosts')

        for timeline in event_timeline or []:
            EventTimelineSerializer(event=event, **timeline).save()

        for hosts in event_hosts or []:
            EventTimelineSerializer(event=event, **hosts).save()

        return event

    def update(self, request, *args, **kwargs):
        event_timeline = request.data.get('event_timeline')
        event_hosts = request.data.get('event_hosts')

        for timeline in event_timeline:
            instance = EventTimeline.objects.get(id=timeline['id'])
            timeline['event'] = instance.event
            EventTimelineSerializer(instance).update(instance, timeline)

        for host in event_hosts:
            instance = EventHost.objects.get(id=host['id'])
            host['event'] = instance.event
            EventHostSerializer().update(instance, host)

        return super().update(request, *args, **kwargs)


class EventTimelineViewSet(ModelViewSet):
    queryset = EventTimeline.objects.all()
    serializer_class = EventTimelineSerializer


class EventHostViewSet(ModelViewSet):
    queryset = EventHost.objects.all()
    serializer_class = EventHostSerializer
