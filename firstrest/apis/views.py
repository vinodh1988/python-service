from django.shortcuts import render
from firstrest.models import Product,Supplier
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from firstrest.apis.serializer import ProductSerializer,SupplierSerializer
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
        try:
            if item.is_valid():
                item.save()
                return Response(item.data)
            else:
                return Response(item.errors,status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(item.errors,status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,pk):
        
        try:
            item=Product.objects.get(pk=pk)
            serialized=ProductSerializer(item,data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data) 
        except Product.DoesNotExist:
            return Response({'error':'No Content'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(item.errors)
    
    def delete(self,request,pk):
        try:
            item=Product.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({'error':'No Record Exist'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(item.errors)
    
class  SuppliersAPI(APIView):

    def get(self,request,pk=None):
        if(pk==None):
            supplierlist=Supplier.objects.all()
            result=SupplierSerializer(supplierlist,many=True)
            return Response(result.data)
        else:
            try:
                item=Supplier.objects.get(pk=pk)
                return Response(SupplierSerializer(item).data)
            except Supplier.DoesNotExist:
                return Response({'error':'No Content'}, status=status.HTTP_204_NO_CONTENT)


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