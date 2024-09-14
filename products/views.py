from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    """ Создает новый продукт. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """ Возвращает список всех продуктов. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
