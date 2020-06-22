from rest_framework import permissions

from event.models import Event
from gallery.models import GalleryPermissions


class UserLevelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return not request.data.get('user') or request.user.id == int(request.data['user'])

        return True


class EventLevelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            event_id = request.data.get('event')
            event = event_id and Event.objects.filter(id=event_id).first()

            return not event or request.user.id == event.user.id

        return True


class GalleryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        event_id = view.kwargs.get('pk')
        return GalleryPermissions.objects.filter(event_id=event_id, user=request.user)
