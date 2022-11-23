from rest_framework import serializers
from .models import Province


class ProvinceSerializer(serializers.ModelSerializer):
    cities = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Province
        fields = ['name', 'cities']
