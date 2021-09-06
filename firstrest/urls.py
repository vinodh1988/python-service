
from django.urls import path
from firstrest.views import getAll

urlpatterns = [
    path('all/',getAll,name="product-list")
]