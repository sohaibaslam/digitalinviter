from rest_framework.serializers import ModelSerializer

from event.models import Event, EventTimeline, EventHost


class EventTimelineSerializer(ModelSerializer):
    class Meta:
        model = EventTimeline
        fields = '__all__'


class EventHostSerializer(ModelSerializer):
    class Meta:
        model = EventHost
        fields = '__all__'


class EventSerializer(ModelSerializer):
    event_timeline = EventTimelineSerializer(many=True, read_only=True)
    event_hosts = EventHostSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
