from django.shortcuts import render
from firstrest.models import Product
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from firstrest.apis.serializer import ProductSerializer
from rest_framework import status

class  ProductsAPI(APIView):

    def get(self,request,pk=None):
        if(pk==None):
            productlist=Product.objects.all()
            result=ProductSerializer(productlist,many=True)
            return Response(result.data)
        else:
            try:
                item=Product.objects.get(pk=pk)
                return Response(ProductSerializer(item).data)
            except Product.DoesNotExist:
                return Response({'error':'No Content'}, status=status.HTTP_204_NO_CONTENT)

    
    def post(self,request):
        item=ProductSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(item.errors)
        

# @api_view(['GET','POST'])
# def products(request):
#     if request.method == 'GET':
#         productlist=Product.objects.all()
#         result=ProductSerializer(productlist,many=True)
#         return Response(result.data)
    
#     if request.method == 'POST':
#         item=ProductSerializer(data=request.data)
#         if item.is_valid():
#             item.save()
#             return Response(item.data)
#         else:
#             return Response(item.errors)