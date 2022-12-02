from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'user', 'province', 'city', 'district', 'title', 'description', 'price', 'category',
                  'is_active_chat', 'is_show_phone']
