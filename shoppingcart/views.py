from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = cart.objects.all()

