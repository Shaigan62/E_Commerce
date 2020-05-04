from products.serializers import ProductSerializer
from products.models import Product
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import generics

class SearchProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ['name']


