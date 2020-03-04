from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from digitalinviter.permissions import UserLevelPermission, EventLevelPermission
from greetings.models import Greeting
from greetings.serializers import GreetingsSerializer


class GreetingsViewSet(ModelViewSet):
    serializer_class = GreetingsSerializer
    queryset = Greeting.objects.all()
    permission_classes = [UserLevelPermission, EventLevelPermission]

    @action(detail=True)
    def get_event_greetings(self, request, pk=None):
        greetings = self.get_queryset().filter(event=pk).values('user__username', 'user__profile_url', 'message')
        return Response(greetings)
