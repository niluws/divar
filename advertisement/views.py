from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from advertisement.serializers import AdvertisementSerializer
from advertisement.models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    """ advertisement from Advertisement model """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['location_id', 'category_id']

    def get_serializer_context(self):
        return {'request': self.request}
