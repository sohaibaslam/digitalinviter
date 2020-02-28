from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def get_user_info(self, request, *args, **kwargs):
        user = self.get_queryset().filter(id=request.user.id).values('id', 'username', 'first_name',
                                                                     'last_name', 'phone_number')
        return Response(user[0] if user else {})

    @action(['PUT'], detail=False)
    def set_phone_number(self, request, *args, **kwargs):
        phone_number = request.data['cellphone']
        request.user.phone_number = phone_number
        request.user.save()

        return Response(status=status.HTTP_200_OK)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.LOGIN_REDIRECT_URL
