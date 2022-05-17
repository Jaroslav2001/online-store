# from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .models import (
    Category,
    Product,
    PropertiesKey,
    PropertiesValue,
)

from .serializers import (
    UserSerializer,
    GroupSerializer,

    CategorySerializer,
    ProductSerializer,
    PropertiesKeySerializer,
    PropertiesValueSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PropertiesKeyViewSet(viewsets.ModelViewSet):
    queryset = PropertiesKey.objects.all()
    serializer_class = PropertiesKeySerializer
    permission_classes = [
        permissions.IsAdminUser |
        permissions.DjangoModelPermissions
    ]


class PropertiesValueViewSet(viewsets.ModelViewSet):
    queryset = PropertiesValue.objects.all()
    serializer_class = PropertiesValueSerializer
    permission_classes = [
        permissions.IsAdminUser |
        permissions.DjangoModelPermissions
    ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAdminUser |
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAdminUser |
        permissions.DjangoModelPermissionsOrAnonReadOnly
    ]
