from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from digitalinviter.permissions import UserLevelPermission, GalleryPermission
from gallery.serializers import GallerySerializer, GalleryPermissionSerializer
from gallery.models import Gallery, GalleryPermissions
from features.models import Feature
from event.models import Event


class GalleryViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [UserLevelPermission, GalleryPermission]

    def create(self, request, *args, **kwargs):
        event = Event.objects.get(id=request.data['event'])
        total_images = Gallery.objects.filter(event=event).count()
        allowed_images = Feature.objects.get(plan=event.plan).features['album_images']

        if total_images < allowed_images:
            if request.data['user'] == request.user.id:
                request.data['is_approved'] = True
            return super().create(request, *args, **kwargs)

        return Response(data={'message': 'Album has reached maximum number of images.'})

    @action(detail=True)
    def get_event_gallery(self, request, pk=None):
        gallery = self.get_queryset().filter(event=pk).values('id', 'user__username', 'user__profile_url', 'image')
        return Response(gallery)

    def get_event_pending_gallery(self, request, pk=None):
        gallery = self.get_queryset().filter(event=pk, is_approved=False).values(
            'user__username',
            'user__profile_url',
            'image',
            'id'
        )

        return Response(gallery)


class GalleryPermissionViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = GalleryPermissions.objects.all()
    serializer_class = GalleryPermissionSerializer
    permission_classes = [UserLevelPermission]

    @action(detail=True)
    def get_event_gallery_permission(self, request, pk=None):
        event = Event.objects.get(id=pk)
        data = GalleryPermissions.objects.filter(event=event, is_allowed=False).values(
            'user_id', 'user__username', 'user__profile_url', 'event_id'
        )
        return Response(data)
