from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    serializer_class = ProductDetailsSerializer
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


@api_view(['POST'])
def ProductFilterViewSet(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        pro = Product.objects.filter(name='screen1')

        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

