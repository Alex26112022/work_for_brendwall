from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductListAPIView, ProductCreateAPIView

app_name = ProductsConfig.name

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('product/create/', ProductCreateAPIView.as_view(),
         name='product_create')
]
