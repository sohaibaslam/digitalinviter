from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from greetings.models import Greeting
from greetings.serializers import GreetingsSerializer


class GreetingsViewSet(ModelViewSet):
    serializer_class = GreetingsSerializer
    queryset = Greeting.objects.all()

    @action(detail=True)
    def get_event_greetings(self, request, pk=None):
        greetings = self.get_queryset().filter(event=pk).values('user__username', 'user__profile_url', 'message')
        return Response(greetings)

    def get_queryset(self):
        return Greeting.objects.filter(Q(is_approved=True) | Q(user=self.request.user))
