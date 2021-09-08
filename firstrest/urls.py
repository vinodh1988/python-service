
from django.urls import path
from firstrest.apis.views import ProductsAPI,SuppliersAPI
from firstrest.apis.genericviews import ProductGAPI
urlpatterns = [
    path('products/',ProductsAPI.as_view(),name="product-list"),
    path('products/<int:pk>',ProductsAPI.as_view(), name="product-by-id"),
    path('suppliers/',SuppliersAPI.as_view(),name="supplier-get"),
    path('market-products/',ProductGAPI.as_view(),name="product-generic"),
    path('market-products/<str:type>/',ProductGAPI.as_view(), name="gproduct-by-type")
]