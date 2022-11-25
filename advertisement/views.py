from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from advertisement.serializers import AdvertisementSerializer
from advertisement.models import Advertisement
from .filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = AdvertisementFilter
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    search_fields=['title','description','category']
    ordering_fields=['price']
    pagination_class = PageNumberPagination
    def get_serializer_context(self):
        return {'request': self.request}
