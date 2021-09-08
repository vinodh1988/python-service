from django.db.models import fields
from rest_framework import serializers
from firstrest.models import Product,Supplier
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
    def validate(self,data):
        if data['price']<0:
            print('validated ', data['price'])
            raise serializers.ValidationError('Price is less than zero')
        else:
            return data
    def validate_type(self,value):
        if value in ['Stationery','Grocery','Electronics','Cosmetics']:
            return value
        else:
            raise serializers.ValidationError("Type value is not correct")


class SupplierSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model= Supplier
        fields= "__all__"
    