from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework import status
from houses.models import House
from houses.serializers import HouseSerializer


class HousesView(APIView):

    def get(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = HouseSerializer(data=request.data)
            if serializer.is_valid():
                house = serializer.save(user=request.user)
                house_serializer = HouseSerializer(house).data
                return Response(data=house_serializer, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
