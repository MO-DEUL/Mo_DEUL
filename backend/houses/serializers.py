from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import House


class HouseSerializer(serializers.ModelSerializer):

    host = TinyUserSerializer()

    class Meta:
        model = House
        fields = ('id', 'host', 'name', 'price', 'address')


class BigHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ('__all__')
