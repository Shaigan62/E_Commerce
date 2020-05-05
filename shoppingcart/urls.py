from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('cart',CartViewSet,basename='cart')

urlpatterns = [
    path('',include(router.urls)),

]