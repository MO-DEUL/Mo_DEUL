from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer
from houses.models import House
from houses.serializers import HouseSerializer


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(UserSerializer(new_user).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UserSerializer(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDetailView(APIView):

    def get(self, request):
        try:
            user = User.objects.get(pk=pk)
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
