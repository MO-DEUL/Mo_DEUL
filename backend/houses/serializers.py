from rest_framework import serializers
from users.serializers import HouseUserSerializer
from .models import House


class HouseSerializer(serializers.ModelSerializer):

    host = HouseUserSerializer()

    class Meta:
        model = House
        exclude = ()
        # fields = ('id', 'host', 'name', 'price', 'address')
        read_only_fields = ("host", 'id', 'created', 'updated')
