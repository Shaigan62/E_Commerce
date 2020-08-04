from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShipmentViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment_Details.objects.all()

class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = Order_Details.objects.all()


class CustomerOrdersViewSet(APIView):
    def get(self,request):
        current_user = request.user
        if current_user.is_authenticated:
            orders = Order.objects.filter(user_id=current_user.id)
            serializer = OrderSerializer(orders,many=True)
            data = serializer.data
            return Response(data)
        else:
            return JsonResponse({"message":"Not Logged In"})