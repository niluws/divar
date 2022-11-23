from rest_framework import serializers
from .models import Category


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    children = ParentSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'children']
