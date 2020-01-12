from rest_framework.serializers import ModelSerializer

from rsvp.models import RSVP


class RSVPSerializer(ModelSerializer):
    class Meta:
        model = RSVP
        fields = '__all__'
