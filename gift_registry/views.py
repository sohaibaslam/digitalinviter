from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from digitalinviter.permissions import UserLevelPermission
from .models import GiftItem, GiftBooking
from .serializers import GiftItemSerializer, GiftBookingSerializer


class GiftItemViewSet(ModelViewSet):
    serializer_class = GiftItemSerializer
    queryset = GiftItem.objects.all()
    permission_classes = [UserLevelPermission]

    @action(detail=True)
    def get_event_gifts(self, request, pk=None):
        offset = int(request.GET.get('offset', 0))
        limit = 6

        gift_items = self.get_queryset().filter(event=pk).values('id', 'name', 'event_id')
        total = gift_items.count()
        gift_items = [gift_item for gift_item in gift_items][offset:offset + limit]

        output = {
            'total': total,
            'gallery': gift_items,
            'next': offset + limit if total - offset > limit else None,
            'previous': offset - limit if offset >= limit else None,
        }
        return Response(output)


class GiftBookingViewSet(ModelViewSet):
    serializer_class = GiftBookingSerializer
    queryset = GiftBooking.objects.all()
    permission_classes = [UserLevelPermission]

    @action(detail=True)
    def get_gift_bookings(self, request, pk=None):
        offset = int(request.GET.get('offset', 0))
        limit = 6

        bookings = self.get_queryset().filter(registry_id=pk).values('id', 'user__username', 'user__profile_url',
                                                                     'registry')
        total = bookings.count()
        bookings = [booking for booking in bookings][offset:offset + limit]

        output = {
            'total': total,
            'gallery': bookings,
            'next': offset + limit if total - offset > limit else None,
            'previous': offset - limit if offset >= limit else None,
        }
        return Response(output)
