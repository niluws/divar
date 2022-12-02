from rest_framework import serializers
from .models import Province, City, District


class CitySerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['city', 'province']


class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ['district', 'city']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        many=True,
        slug_field='city',

    )

    class Meta:
        model = Province
        fields = ['province', 'cities']

