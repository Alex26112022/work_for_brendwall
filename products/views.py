from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework.generics import CreateAPIView, ListAPIView

from products.models import Product
from products.paginators import MyPaginator
from products.serializers import ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    """ Создает новый продукт. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """ Возвращает список всех продуктов. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPaginator


class ProductListView(ListView):
    """ Отображает список продуктов на странице. """
    model = Product


class ProductCreateView(CreateView):
    """ Форма для создания нового продукта. """
    model = Product
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('products:products_list')
