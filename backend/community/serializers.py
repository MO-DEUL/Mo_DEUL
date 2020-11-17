from rest_framework import serializers
from .models import Community, Comment


class CommunitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
