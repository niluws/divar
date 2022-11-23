from rest_framework.viewsets import ModelViewSet
from .serializers import ProvinceSerializer, CitySerializer
from .models import Province, City


class ProvinceView(ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_serializer_context(self):
        return {'request': self.request}
