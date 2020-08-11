from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    queryset = FAQ.objects.all()