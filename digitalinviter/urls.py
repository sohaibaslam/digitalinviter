"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from event.views import EventViewSet, EventTimelineViewSet, EventHostViewSet, ThemeImageViewSet, privacy_policy
from rsvp.views import RSVPViewSet
from users.views import UserViewSet
from themes.views import ThemeViewSet
from users.views import FacebookLogin
from greetings.views import GreetingsViewSet
from gallery.views import GalleryViewSet


router = DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'users', UserViewSet)
# router.register(r'event_timeline', EventTimelineViewSet)
# router.register(r'event_host', EventHostViewSet)
router.register(r'rsvp', RSVPViewSet)
router.register(r'theme', ThemeViewSet)
router.register(r'greeting', GreetingsViewSet)
router.register(r'theme_image', ThemeImageViewSet)
router.register(r'gallery', GalleryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^privacy-policy', privacy_policy),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
]
if os.environ.get('dev'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
