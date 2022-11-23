from rest_framework import serializers
from .models import Province, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = serializers.HyperlinkedRelatedField(
        queryset=City.objects.all(),
        view_name='city-detail',
        many=True
    )

    class Meta:
        model = Province
        fields = ['name', 'cities']
