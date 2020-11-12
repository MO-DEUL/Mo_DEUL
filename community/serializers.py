from rest_framework import serializers
from .models import Community, Comment


class CommunitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('writer',
                  'title',
                  'post',
                  'time',)


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('writer',
                  'title',
                  'comment',
                  'time',)
