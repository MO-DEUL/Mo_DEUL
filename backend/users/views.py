import os
import requests
from django.views import View
from django.shortcuts import redirect, reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User


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


class LoginView(View):
    # GET /users/login
    def get(self, request):
        pass

    # POST /users/login
    def post(self, request):
        pass


class KaKaoException(Exception):
    pass


def kakao_login(request):
    client_id = os.environ.get("KAKAO_ID")
    redirect_url = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code")


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=KAKAO_ID")
    except KaKaoException:
        return redirect(reverse("users:login"))
