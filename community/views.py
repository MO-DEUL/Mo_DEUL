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
    # GET /comumnity
    # GET /community/{community_id}
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            community_queryset = Community.objects.all()
            community_queryset_serializer = CommunitySerializers(community_queryset, many=True)
            return Response(community_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            community_serializer = CommunitySerializers(Community,objects.get(id=id))
            return Response(community_serializer.data, status=status.HTTP_200_OK)
    
    # PUT /community/{community_id}
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            community_object = Community.objects.get(id=id)

            update_community_serializer = CommunitySerializers(community_object,data=request.data)
            if update_community_serializer.is_valid():
                update_community_serializer.save()
                return Response(update_community_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE /community/{community_id}
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            community_object = Community.objects.get(id=id)
            community_object.delete()
            return Response("deleted", status=status.HTTP_200_OK)

class CommentView():
    
