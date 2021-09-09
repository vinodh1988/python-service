from rest_framework import generics
from firstrest.apis.serializer import ProductSerializer
from firstrest.models import Product

class ProductGAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'type']

    # def get_queryset(self): 
    #     #searchtype = self.kwargs['type']
    #     #searchtype=self.request.query_params.get('type')
    #     if searchtype==None:
    #         return Product.objects.all()
    #     print(searchtype,'#########')
    #     return Product.objects.filter(type=searchtype)