from rest_framework import serializers
from .models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('name',
                  'description',
                  'city',
                  'price',
                  'address',
                  'bedrooms',
                  'baths',
                  'house_type',
                  'amenities',
                  'facilites',
                  'host',
                  'house_type',)
