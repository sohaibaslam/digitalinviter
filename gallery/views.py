from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from digitalinviter.permissions import UserLevelPermission, EventLevelPermission
from gallery.serializers import GallerySerializer
from gallery.models import Gallery


class GalleryViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [UserLevelPermission, EventLevelPermission]

    @action(detail=True)
    def get_event_gallery(self, request, pk=None):
        gallery = self.get_queryset().filter(event=pk).values('user__username', 'user__profile_url', 'image')
        return Response(gallery)
