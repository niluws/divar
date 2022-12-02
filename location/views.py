from .serializers import ProvinceSerializer, CitySerializer, DistrictSerializer
from .models import Province, City, District
from rest_framework.generics import ListAPIView


class ProvinceView(ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

