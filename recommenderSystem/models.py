from django.db import models
from accounts.models import User
from products.models import Product,Category,Brand,Product_Rating
# Create your models here.

class user_activity(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    viewed = models.BooleanField()
    rated = models.BooleanField()
    purchase = models.BooleanField()
    coll_date = models.DateTimeField()      #data collection date

class recommendProd(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    collection_date = models.DateTimeField()
