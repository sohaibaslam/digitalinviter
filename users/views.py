from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://localhost:3000/home'
