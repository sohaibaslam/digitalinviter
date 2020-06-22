from rest_framework.serializers import ModelSerializer

from gallery.models import Gallery, GalleryPermissions


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryPermissionSerializer(ModelSerializer):
    class Meta:
        model = GalleryPermissions
        fields = '__all__'
