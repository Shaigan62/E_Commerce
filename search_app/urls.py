from django.urls import path,include
from .views import *

urlpatterns = [
    path('',SearchProductListView.as_view(), name='searchproduct'),
]