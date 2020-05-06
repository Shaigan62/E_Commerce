from django.contrib import admin
from products.models import *
admin.site.register([Category,Product,Product_Image,Product_Variant,Product_Rating])