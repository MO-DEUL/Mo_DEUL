from rest_framework import serializers
from users.serializers import HouseUserSerializer
from .models import House


class HouseSerializer(serializers.ModelSerializer):

    host = HouseUserSerializer()

    class Meta:
        model = House
        fields = ('id', 'host', 'name', 'price', 'address')
