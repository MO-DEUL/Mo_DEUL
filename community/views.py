from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializers, CommunitySerializers
from .models import Comment, Community


class CommunityView(APIView):
    # POST /community
    def post(self, request):
        community_serializers = CommunitySerializers(data=request.data)
        if community_serializers.is_valid():
            community_serializers.save()
            return Response(community_serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(community_serializers.data, status=status.HTTP_400_BAD_REQUEST)
    
class CommentView():
    
