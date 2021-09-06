from django.db import models

# Create your models here.
class Product(models.Model):
    productid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30,null=False)
    price=models.FloatField(null=False)
    type=models.CharField(null=False,max_length=30)

    def __str__(self):
        return self.name
    
    