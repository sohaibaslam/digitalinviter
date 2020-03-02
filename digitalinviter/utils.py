from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class ObjectLevelPermissionMixin:
    def post(self, request, *args, **kwargs):
        return self.check_ownership(request)

    def put(self, request, *args, **kwargs):
        return self.check_ownership(request)

    def check_ownership(self, request):
        if self.get_object().id == request.user.id:
            return Response(status.HTTP_200_OK)

        raise PermissionDenied
