from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.views import APIView

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

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()




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


class ProductFilterViewSet(APIView):
    def post(self, request):
        post_data = request.data
        priceStart = post_data['priceStart']
        priceEnd = post_data['priceEnd'] if post_data['priceEnd'] > 0 else Product.objects.latest('price').price

        brands = [bid.id for bid in Brand.objects.filter(brand_name__in=post_data['brands'])]
        categories = [cid.id for cid in Category.objects.filter(title__in=post_data['categories'])]

        product = Product.objects.filter(price__range=(priceStart,priceEnd))
        if post_data['brands']:
            product = product.filter(brand__in=brands)
        if post_data['categories']:
            product = product.filter(category__in=categories)

        product = product.order_by('id')

        paginator = PageNumberPagination()
        paginator.page_size = post_data['page_limit']
        result_page = paginator.paginate_queryset(product, request)
        serializer = ProductDetailsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)