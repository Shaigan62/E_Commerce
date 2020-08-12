from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings

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


class GetOrderDetailsViewSet(generics.ListAPIView):
    serializer_class = OrderDetailsSerializer
    lookup_url_kwarg = "oid"
    def get_queryset(self):
        oid = self.kwargs.get(self.lookup_url_kwarg)
        order_details = Order_Details.objects.filter(order_id=oid)
        order_cancel_mail()
        return order_details

class CancelOrder(APIView):
    def post(self,request):
        current_user = request.user
        if current_user.is_authenticated:
            post_data = request.data
            reason = "Reason: " + str(post_data['reason'])+"\n"
            name = "User: "+ str(current_user.username)+"\n"
            user_id ="User_ID: " +str(current_user.id) +"\n"
            order_id = "Order_id: " +str(post_data['order_id'])+"\n"
            message = str(user_id) + str(name) + str(order_id) + str(reason)
            subject = "Order Cancellation"
            order_cancel_mail(subject,message)
            return JsonResponse({"message":"Request sent"})
        else:
            return JsonResponse({"message":"Not Logged In"})


def order_cancel_mail(subject,message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["shaiganyounis15@gmail.com"]
    send_mail(subject, message, email_from, recipient_list)