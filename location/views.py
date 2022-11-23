from rest_framework.generics import ListAPIView
from .serializers import ProvinceSerializer
from .models import Province


class CityProvinceView(ListAPIView):
    """ advertisement from Advertisement model """
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

