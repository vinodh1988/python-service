from django.shortcuts import render
from firstrest.models import Product
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def getAll(Request):
    result=Product.objects.all()
    return JsonResponse({'products':list(result.values())}) 

@api_view(['GET','POST'])
def hello(Request):
    print(Request.data)
    return Response({"Message":"Hello world!!!"})