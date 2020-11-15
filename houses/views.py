from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HouseSerializer
from .models import House


class HouseView(APIView):
    # POST /houses
    def post(self, request):
        house_serializer = HouseSerializer(data=request.data)
        if house_serializer.is_valid():
            house_serializer.save()
            return Response(house_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(house_serializer.error, status=status.HTTP_400_BAD_REQUEST)
