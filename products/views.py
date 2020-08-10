from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes_by_action = {'create': [IsAdminUser],
    #                                 'list': [AllowAny]}
    #
    # def create(self, request, *args, **kwargs):
    #     return super(ProductViewSet, self).create(request, *args, **kwargs)
    #
    # def list(self, request, *args, **kwargs):
    #     return super(ProductViewSet, self).list(request, *args, **kwargs)
    #
    # def get_permissions(self):
    #     try:
    #         # return permission_classes depending on `action`
    #         return [permission() for permission in self.permission_classes_by_action[self.action]]
    #     except KeyError:
    #         # action is not set return default permission_classes
    #         return [permission() for permission in self.permission_classes]


class ProductImageViewSet(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = Product_Image.objects.all()

class ProductVariantViewSet(viewsets.ModelViewSet):
    serializer_class = ProductVariantSerializer
    queryset = Product_Variant.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryViewSet(generics.ListAPIView):
    serializer_class = CategorySerializer
    lookup_url_kwarg = "pid"
    def get_queryset(self):
        pid = self.kwargs.get(self.lookup_url_kwarg)
        sub_cateogry = Category.objects.filter(parent_id=pid)
        return sub_cateogry

class ParentCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent_id__isnull=True)


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
                      .order_by('-user_clicks')
                       )[:5]

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
        if post_data['categories']:
            product = product.filter(category__in=categories)

        if post_data['brands']:
            product = product.filter(brand__in=brands)

        product = product.order_by('id')

        paginator = PageNumberPagination()
        paginator.page_size = post_data['page_limit']
        result_page = paginator.paginate_queryset(product, request)
        serializer = ProductDetailsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)



class IncreaseProductClick(APIView):
    def put(self, request, pk, format=None):
        try:
            snippet = Product.objects.get(pk=pk)
            snippet.user_clicks += 1
            snippet.save()
            serial_data = ProductSerializer(snippet)
            return Response(serial_data.data)
        except Exception:
            return Response({'message':"No Product Found"}, status=status.HTTP_204_NO_CONTENT)




