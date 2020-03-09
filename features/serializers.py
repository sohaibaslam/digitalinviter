from rest_framework.serializers import ModelSerializer

from features.models import Feature


class FeatureSerializer(ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'
