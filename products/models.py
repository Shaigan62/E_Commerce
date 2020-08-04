from django.db import models
from accounts.models import User

class Category(models.Model):
    title = models.CharField(max_length=255)
    parent_id = models.ForeignKey("self",on_delete=models.CASCADE,null=True)
    category_image = models.CharField(max_length=255, null=True, default="")

    def __str__(self):
        return self.title

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_image = models.CharField(max_length=255,null=True,default="")

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(null=True)
    category = models.ForeignKey(Category,related_name='pro_category',on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,related_name='pro_brand',on_delete=models.CASCADE,null=True)
    sold = models.IntegerField(default=0)
    user_clicks = models.IntegerField(default=0)

class Product_Variant(models.Model):
    product_id = models.ForeignKey(Product,related_name='variants',on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size  = models.CharField(max_length=100)

class Product_Image(models.Model):
    img_url = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    sku = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.img_url

class Product_Rating(models.Model):
    rating = models.FloatField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


