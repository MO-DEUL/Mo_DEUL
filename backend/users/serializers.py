from rest_framework import serializers
from .models import User


class HouseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', "superhost")


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "password", "username", "first_name",
                  "last_name", "email", "avatar", "superhost")
        read_only_fields = ("id", "superhost", "avatar")
