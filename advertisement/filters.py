from django_filters.rest_framework import FilterSet
from .models import Advertisement


class AdvertisementFilter(FilterSet):
    class Meta:
        model = Advertisement
        fields = {
            'location_id': ['exact'],
            'category_id': ['exact'],
            'price': ['lt', 'gt']
        }
