from rest_framework import serializers
from .models import Province, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name','state']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = serializers.HyperlinkedRelatedField(
        view_name='city-detail',
        many=True,
        read_only=True


    )

    class Meta:
        model = Province
        fields = ['name', 'cities']
