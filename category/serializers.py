from rest_framework import serializers
from .models import Category


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class CategorySerializer(serializers.ModelSerializer):
    subcategory = ParentSerializer(many=True)

    class Meta:
        model = Category
        fields = ['category', 'subcategory']

