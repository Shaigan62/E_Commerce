from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = Product_Image.objects.all()

class ProductVariantViewSet(viewsets.ModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = Product_Variant.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = Product_Rating.objects.all()


class TopProductViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        product_top = (Product.objects
                      .order_by('-sold')
                      .values_list('sold', flat=True)
                      .distinct())
        product_top = list(product_top)
        product_top =(Product.objects
                      .order_by('-sold')
                      .filter(sold__in=product_top[:3]))

        return product_top


class ProductDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProductDetailsSerializer
    queryset = Product.objects.all()


class ProductByCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductByCategorySeializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title']