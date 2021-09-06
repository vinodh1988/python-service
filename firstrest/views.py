from django.shortcuts import render
from firstrest.models import Product
from django.http import JsonResponse

# Create your views here.
def getAll(Request):
    result=Product.objects.all()
    return JsonResponse({'products':list(result.values())}) 