from rest_framework.serializers import ModelSerializer
from .models import Theme


class ThemeSerializer(ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
