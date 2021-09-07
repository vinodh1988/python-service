from rest_framework import serializers
from firstrest.models import Product
# class ProductSerializer(serializers.Serializer):
#     productid=serializers.IntegerField()
#     name=serializers.CharField()
#     price=serializers.FloatField()
#     type=serializers.CharField()

#     def create(self, data):
#         return Product.objects.create(**data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = "__all__" 
        #exclude=['productid']   
    