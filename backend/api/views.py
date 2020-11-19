from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend.users.serializers import UserSerializer
from backend.users.models import User
from backend.houses.serializers import HouseSerializer
from backend.houses.models import House


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
