from django.shortcuts import render
from firstrest.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstrest.apis.serializer import ProductSerializer
@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        productlist=Product.objects.all()
        result=ProductSerializer(productlist,many=True)
        return Response(result.data)
    
    if request.method == 'POST':
        item=ProductSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(item.errors)