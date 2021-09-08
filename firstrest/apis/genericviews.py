from rest_framework import generics
from firstrest.apis.serializer import ProductSerializer
from firstrest.models import Product

class ProductGAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer