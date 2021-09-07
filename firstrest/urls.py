
from django.urls import path
from firstrest.apis.views import ProductsAPI

urlpatterns = [
    path('',ProductsAPI.as_view(),name="product-list"),
    path('<int:pk>',ProductsAPI.as_view(), name="product-by-id")
]