from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('registeractivity/<int:proid>/',RegisterActivityViewSet.as_view(),name='regsiteractivity'),
    path('recommendproduct/',RecommendProduct.as_view(),name='recommendproduct')
]