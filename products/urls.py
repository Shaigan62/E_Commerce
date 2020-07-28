from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product',ProductViewSet,basename='product')
router.register('productimage',ProductImageViewSet,basename='product_image')
router.register('productvariant',ProductVariantViewSet,basename='product_variant')
router.register('category',CategoryViewSet,basename='category')
router.register('rating',ProductRatingViewSet,basename='rating')
router.register('details',ProductDetailViewSet,basename='details')                          #get details of product like image and variants
router.register('categoryproduct',ProductByCategoryViewSet,basename='categoryproduct')      #products that belongs to a specific category
router.register('brand',BrandViewSet,basename='brand')
router.register('parentcategory',ParentCategoryViewSet,basename='parentcategory')
urlpatterns = [
    path('',include(router.urls)),
    path('topproducts/',TopProductViewSet.as_view(), name='topproducts'),                   #top 3 products based on product clicks
    path('filter/',ProductFilterViewSet.as_view(), name='filter'),
    path('productclick/<int:pk>/',IncreaseProductClick.as_view(),name='productclick'),
    path('subcategory/<int:pid>/',SubCategoryViewSet.as_view(),name='subcategory'),
]