from django.db import models
from accounts.models import User
from products.models import Product,Product_Variant

class Order(models.Model):
    created_at = models.DateTimeField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Shipment_Details(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255,default="Pakistan")
    city = models.CharField(max_length=255)
    address = models.TextField()

class Order_Details(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    product_variant_id = models.ForeignKey(Product_Variant,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
