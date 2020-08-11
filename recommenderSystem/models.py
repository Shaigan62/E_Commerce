from django.db import models
from accounts.models import User
from products.models import Product,Category,Brand,Product_Rating

from datetime import datetime

class user_activity(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    activity_time = models.DateTimeField(auto_now_add=True)