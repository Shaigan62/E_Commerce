from .serializers import *
from rest_framework import viewsets

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShipmentViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment_Details.objects.all()

class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = Order_Details.objects.all()
