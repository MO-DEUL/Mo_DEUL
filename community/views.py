from rest_framework import viewsets
from .serializers import CommentSerializers, CommunitySerializers
from .models import Comment, Community


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
