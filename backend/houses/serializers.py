from rest_framework import serializers
from users.serializers import HouseUserSerializer
from .models import House, Amenity, Facility


class HouseAmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = ('name',)


class HouseFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ('name',)


class HouseSerializer(serializers.ModelSerializer):

    host = HouseUserSerializer()
    amenities = HouseAmenitySerializer()
    facilites = HouseFacilitySerializer()

    class Meta:
        model = House
        exclude = ()
        # fields = ('id', 'host', 'name', 'price', 'address')
        read_only_fields = ("host", 'id', 'created', 'updated')
