from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('order',OrderViewSet,basename='order')
router.register('shipment',ShipmentViewSet,basename='shipment_details')
router.register('orderdetails',OrderDetailsViewSet,basename='order_details')

urlpatterns = [
    path('',include(router.urls)),
    path('customerorders/',CustomerOrdersViewSet.as_view(),name='customerorders'),
]