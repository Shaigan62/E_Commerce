from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product',ProductViewSet,basename='product')
router.register('productimage',ProductImageViewSet,basename='product_image')
router.register('productvariant',ProductVariantViewSet,basename='product_variant')
router.register('category',CategoryViewSet,basename='category')
router.register('rating',ProductRatingViewSet,basename='rating')
urlpatterns = [
    path('',include(router.urls)),
    path('topproducts/',TopProductViewSet.as_view(), name='topproducts'),

]