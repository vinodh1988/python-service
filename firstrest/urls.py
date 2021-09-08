
from django.urls import path
from firstrest.apis.views import ProductsAPI,SuppliersAPI

urlpatterns = [
    path('products/',ProductsAPI.as_view(),name="product-list"),
    path('products/<int:pk>',ProductsAPI.as_view(), name="product-by-id"),
    path('suppliers/',SuppliersAPI.as_view(),name="supplier-get")
]