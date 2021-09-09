from rest_framework import generics
from firstrest.apis.serializer import ProductSerializer
from firstrest.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from firstrest.apis.pagination import ProductSetPagination,CursorPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
class ProductGAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #filter_backends = [DjangoFilterBackend]
    #throttle_classes = [UserRateThrottle,AnonRateThrottle]
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['name', 'type']
    search_fields=['name','type']
    pagination_class=  ProductSetPagination
    ordering_fields=['name','type','price']
    # def get_queryset(self): 
    #     #searchtype = self.kwargs['type']
    #     #searchtype=self.request.query_params.get('type')
    #     if searchtype==None:
    #         return Product.objects.all()
    #     print(searchtype,'#########')
    #     return Product.objects.filter(type=searchtype)