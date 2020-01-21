from rest_framework.viewsets import ModelViewSet
from .models import Theme
from .serializers import ThemeSerializer


class ThemeViewSet(ModelViewSet):
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
