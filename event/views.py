from rest_framework.viewsets import ModelViewSet


from event.serializers import EventSerializer, EventTimelineSerializer, EventHostSerializer
from event.models import Event, EventTimeline, EventHost


class EventViewSet(ModelViewSet):
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventSerializer


class EventTimelineViewSet(ModelViewSet):
    queryset = EventTimeline.objects.all()
    serializer_class = EventTimelineSerializer


class EventHostViewSet(ModelViewSet):
    queryset = EventHost.objects.all()
    serializer_class = EventHostSerializer
