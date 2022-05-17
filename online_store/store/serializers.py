from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import (
    Category,
    Product,
    PropertiesKey,
    PropertiesValue,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PropertiesKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertiesKey
        fields = ['url', 'name', 'description']


class PropertiesValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertiesValue
        fields = ['url', 'properties_key', 'value']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description', 'img']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'name', 'price', 'description', 'category', 'properties', 'img']
