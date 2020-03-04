from rest_framework.serializers import ModelSerializer

from greetings.models import Greeting


class GreetingsSerializer(ModelSerializer):
    class Meta:
        model = Greeting
        fields = '__all__'
