from django.contrib import admin
from orders.models import *
admin.site.register([Order,Order_Details,Shipment_Details])