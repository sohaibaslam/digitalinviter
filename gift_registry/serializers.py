from rest_framework.serializers import ModelSerializer

from gift_registry.models import GiftItem, GiftBooking


class GiftItemSerializer(ModelSerializer):
    class Meta:
        model = GiftItem
        fields = '__all__'


class GiftBookingSerializer(ModelSerializer):
    class Meta:
        model = GiftBooking
        fields = '__all__'
