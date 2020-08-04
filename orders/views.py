from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShipmentViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment_Details.objects.all()

class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = Order_Details.objects.all()


class CustomerOrdersViewSet(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        current_user = self.request.user

        if current_user.is_authenticated:
            orders = Order.objects.filter(user_id=current_user.id)
            return orders
        else:
            return "Please Login"