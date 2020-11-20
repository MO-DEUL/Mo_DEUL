from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.users.serializers import UserSerializer
from backend.users.models import User
from backend.houses.serializers import HouseSerializer
from backend.houses.models import House
from backend.community.serializers import CommentSerializers, CommunitySerializers
from backend.community.models import Comment, Community


class UserView(APIView):
    # POST /users
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # GET/users
    # GET/users/{user_id}
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            user_queryset = User.objects.all()
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            user_serializer = UserSerializer(User.objects.get(id=id))
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    # PUT /users/{user_id}
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            user_object = User.objects.get(id=id)

            update_user_serializer = UserSerializer(
                user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    # DELETE /users/{user_id}

    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            user_object = User.objects.get(id=id)
            user_object.delete()
            return Response("deleted", status=status.HTTP_200_OK)


class HouseView(APIView):
    # POST /houses
    def post(self, request):
        house_serializer = HouseSerializer(data=request.data)
        if house_serializer.is_valid():
            house_serializer.save()
            return Response(house_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(house_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # GET /houses
    # GET /houses/{house_id}
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            house_queryset = House.objects.all()
            house_queryset_serializer = HouseSerializer(
                house_queryset, many=True)
            return Response(house_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            house_serializer = HouseSerializer(House.objects.get(id=id))
            return Response(house_serializer.data, status=status.HTTP_200_OK)

    # PUT /houses/{house_id}
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            house_object = House.objects.get(id=id)

            update_house_serializer = HouseSerializer(
                house_object, data=request.data)
            if update_house_serializer.is_valid():
                update_house_serializer.save()
                return Response(update_house_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)

    # DELETE /houses/{house_id}
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            house_object = House.objects.get(id=id)
            house_object.delete()
            return Response("deleted", status=status.HTTP_200_OK)


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
            community_queryset_serializer = CommunitySerializers(
                community_queryset, many=True)
            return Response(community_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            community_serializer = CommunitySerializers(
                Community.objects.get(id=id))
            return Response(community_serializer.data, status=status.HTTP_200_OK)

    # PUT /community/{community_id}
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            community_object = Community.objects.get(id=id)

            update_community_serializer = CommunitySerializers(
                community_object, data=request.data)
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


class CommentView(APIView):
    # POST /community/comment
    def post(self, request, **kwargs):
        comment_serializer = CommentSerializers(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # GET /community/comment
    # GET /community/comment/{comment_id}
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            comment_queryset = Comment.objects.all()
            comment_queryset_serializer = CommentSerializers(
                comment_queryset, many=True)
            return Response(comment_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('id')
            comment_serializer = CommentSerializers(Comment.objects.get(id=id))
            return Response(comment_serializer.data, status=status.HTTP_200_OK)

    # PUT /community/comment/{comment_id}
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            comment_object = Comment.objects.get(id=id)

            update_comment_serializer = CommentSerializers(
                comment_object, data=request.data)
            if update_comment_serializer.is_valid():
                update_comment_serializer.save()
                return Response(update_comment_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    # DELETE /community/comment/{comment_id}
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            id = kwargs.get('id')
            comment_object = Comment.objects.get(id=id)
            comment_object.delete()
            return Response("deleted", status=status.HTTP_200_OK)
