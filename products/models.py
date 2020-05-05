from django.db import models
from accounts.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    parent_id = models.ForeignKey("self",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category,related_name='pro_category',on_delete=models.CASCADE)
    sold = models.IntegerField(default=0)
    user_clicks = models.IntegerField(default=0)

class Product_Variant(models.Model):
    product_id = models.ForeignKey(Product,related_name='variants',on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size  = models.CharField(max_length=100)

class Product_Image(models.Model):
    img_url = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)

    def __str__(self):
        return self.img_url

class Product_Rating(models.Model):
    rating = models.FloatField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
