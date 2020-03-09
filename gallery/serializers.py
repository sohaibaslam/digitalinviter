from rest_framework.serializers import ModelSerializer

from gallery.models import Gallery


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
