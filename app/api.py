from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Temperature
from .serializer import Dht11serialize


@api_view(['GET'])
def Dlist(request):
    all_data = Temperature.objects.all()
    data = Dht11serialize(all_data, many=True).data
    return Response({'data': data})


class Dhtviews(generics.CreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = Dht11serialize
