
from django.urls import path
from firstrest.apis.views import products

urlpatterns = [
    path('',products,name="product-list")
]