from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


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
    def get(self, request):
        return Response("test ok", status=200)

    # PUT /users/{user_id}
    def put(self, request):
        return Response("test ok", status=200)

    # DELETE /users/{user_id}
    def delete(self, request):
        return Response("test ok", status=200)
