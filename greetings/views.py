from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from greetings.models import Greeting
from event.models import Event
from greetings.serializers import GreetingsSerializer


class GreetingsViewSet(ModelViewSet):
    serializer_class = GreetingsSerializer
    queryset = Greeting.objects.all()

    @action(detail=True)
    def get_event_greetings(self, request, pk=None):
        query = self.get_queryset().filter(event=pk)

        if not request.user.is_authenticated:
            query = query.filter(is_approved=True)
        elif not Event.objects.filter(id=pk).filter(user=request.user):
            query = query.filter(Q(is_approved=True) | Q(user=request.user))

        greetings = query.values('id', 'user__username', 'user__profile_url', 'message', 'is_approved')
        return Response(greetings)
