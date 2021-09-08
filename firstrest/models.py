from django.db import models

class Supplier(models.Model):
    supplierid=models.AutoField(primary_key=True),
    name=models.CharField(max_length=30,null=False)
    city=models.CharField(max_length=30,null=False)
    address=models.CharField(max_length=60,null=False)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    productid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    price=models.FloatField(null=False)
    type=models.CharField(null=False,max_length=30)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


    
    