from django.db import models
from accounts.models import User
from products.models import Product,Product_Variant


class cart(models.Model):
    member_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_varaint_id = models.ForeignKey(Product_Variant,on_delete=models.CASCADE)

