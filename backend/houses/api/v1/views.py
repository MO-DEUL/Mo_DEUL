from rest_framework.generics import ListAPIView, RetrieveAPIView

from houses.serializers import HouseSerializer
from houses.models import House


class ListHousesView(ListAPIView):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
