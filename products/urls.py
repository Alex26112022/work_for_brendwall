from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductListAPIView, ProductCreateAPIView, \
    ProductListView, ProductCreateView

app_name = ProductsConfig.name

urlpatterns = [
    path('api/products/', ProductListAPIView.as_view(),
         name='api_products_list'),
    path('api/product/create/', ProductCreateAPIView.as_view(),
         name='api_product_create'),
    path('', ProductListView.as_view(), name='products_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
]
