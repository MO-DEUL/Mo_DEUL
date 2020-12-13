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


class HouseView(APIView):

    def get_house(self, pk):
        try:
            house = House.objects.get(pk=pk)
            return house
        except House.DoesNotExist:
            return None

    def get(self, request, pk):
        house = self.get_house(pk)
        if house is not None:
            serializer = HouseSerializer(house).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        house = self.get_house(pk)
        if house is not None:
            if house.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = HouseSerializer(
                house, data=request.data, partial=True)
            if serializer.is_valid():
                house = serializer.save()
                return Response(HouseSerializer(house).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
