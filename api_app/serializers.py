from rest_framework import serializers
from api_app.models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
